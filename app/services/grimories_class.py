from fastapi.responses import JSONResponse

from app.models.db import Grimoires as GrimoireDB, Applications as ApplicationsDB


class Grimoire:
    def __init__(self):
        pass

    def all_grimoire(self):
        res = []
        try:
            query = GrimoireDB.select().dicts()
            for row in query:
                res.append(row)
            return JSONResponse(status_code=200, content=res)
        except Exception as exp:
            return JSONResponse(status_code=404, content={'detail': [{'msg': str(exp)}]})

    def assignment_grimories(self):
        res = {}
        try:
            query = ApplicationsDB.select(ApplicationsDB.name, GrimoireDB.grimoire_name, GrimoireDB.front_name) \
                .join(GrimoireDB, on=(ApplicationsDB.grimoires_id == GrimoireDB.id)) \
                .order_by(GrimoireDB.grimoire_name).dicts()
            for row in query:
                data = [{'name': row['name'],
                         'front_name': row['front_name']}]
                if row['grimoire_name'] in res:
                    res[row['grimoire_name']] = res[row['grimoire_name']] + data
                else:
                    res[row['grimoire_name']] = data
            return JSONResponse(status_code=200, content=res)
        except Exception as exp:
            return JSONResponse(status_code=404, content={'detail': [{'msg': str(exp)}]})
