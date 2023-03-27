from fastapi import APIRouter

from app.services.grimories_class import Grimoire

router = APIRouter()


# GET
@router.get(path='/')
async def all_grimoires():
    object_grimoire = Grimoire()
    return object_grimoire.all_grimoires()


@router.get(path='/assignment')
async def assignment_grimoires():
    object_grimoire = Grimoire()
    return object_grimoire.assignment_grimories()
