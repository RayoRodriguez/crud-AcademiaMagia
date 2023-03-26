from fastapi import APIRouter
from app.services.grimories_class import Grimoire


router = APIRouter()

#GET
@router.get(path='/')
async def all_grimories():
    object_Grimorie = Grimoire()
    return object_Grimorie.all_grimoires()

@router.get(path='/assignment')
async def assignment_grimories():
    object_Grimorie = Grimoire()
    return object_Grimorie.assignment_grimories()

#POST


#PUT


#DELETE
