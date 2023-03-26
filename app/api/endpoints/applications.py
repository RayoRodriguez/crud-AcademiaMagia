from fastapi import APIRouter


router = APIRouter()

#GET
@router.get(path='/')
async def get_all_applications():
    return ('hola')