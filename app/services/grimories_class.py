from app.models.db import Grimoires as GrimoiresDB
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