from fastapi import APIRouter

from app.services.affinities_class import Affinities as AffinitiesClass

router = APIRouter()


# GET
@router.get(path='/')
async def all_affinities():
    object_affinities = AffinitiesClass()
    return object_affinities.all_afinities()
