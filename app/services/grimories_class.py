from app.models.db import Grimoires as GrimoiresDB, Applications as ApplicationsDB
from fastapi.responses import JSONResponse


class Grimoire:
    def __init__(self):
        pass

    def all_grimoires(self):
        res = []
        try:
            query = GrimoiresDB.select().dicts()
            for row in query:
                res.append(row)
            return JSONResponse(status_code = 200, content = res)
        except Exception as exep:
            return JSONResponse(status_code = 404, content = str(exep))
        
    def assignment_grimories(self):
        res = {}
        try:
            query = ApplicationsDB.select(ApplicationsDB.name, GrimoiresDB.grimoire_name, GrimoiresDB.front_name)\
                .join(GrimoiresDB, on = (ApplicationsDB.grimoires_id == GrimoiresDB.id))\
                .order_by(GrimoiresDB.grimoire_name).dicts()
            for row in query:
                data = [{'name': row['name'], 
                        'front_name': row['front_name']}]
                if row['grimoire_name'] in res:
                    res[row['grimoire_name']] = res[row['grimoire_name']] + data
                else:
                    res[row['grimoire_name']] = data
            return JSONResponse(status_code = 200, content = res)
        except Exception as exep:
            return JSONResponse(status_code = 404, content = str(exep))