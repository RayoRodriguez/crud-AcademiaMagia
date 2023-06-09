from fastapi.responses import JSONResponse

from app.models.db import MagicAffinities as MagicAffinitiesDB


class Affinities:
    def __init__(self):
        pass

    def all_afinities(self):
        res = []
        try:
            query = MagicAffinitiesDB.select().dicts()
            for row in query:
                res.append(row)
            return JSONResponse(status_code=200, content=res)
        except Exception as exp:
            return JSONResponse(status_code=404, content={'detail': [{'msg': str(exp)}]})
