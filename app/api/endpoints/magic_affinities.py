from fastapi import APIRouter
from app.services.affinities_class import Affinities as AffinitiesClass


router = APIRouter()

#GET
@router.get(path='/')
async def all_affinities():
    object_Affinities = AffinitiesClass()
    return object_Affinities.all_afinities()

#POST


#PUT


#DELETE