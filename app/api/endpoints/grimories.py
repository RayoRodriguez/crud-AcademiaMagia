from fastapi import APIRouter
from app.services.grimories_class import Grimoire


router = APIRouter()
object_Grimorie = Grimoire()

#GET
@router.get(path='/')
async def all_gremories():
    return object_Grimorie.all_grimoires()

#POST


#PUT


#DELETE
