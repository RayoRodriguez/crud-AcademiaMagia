from fastapi import APIRouter
from app.models.db import Grimoires


router = APIRouter()

#GET
@router.get(path='/')
async def get_all_applications():
    res = []
    query = Grimoires.select().dicts()
    for row in query:
        res.append(row)
    return (res)