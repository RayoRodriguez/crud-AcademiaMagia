from fastapi import APIRouter


router = APIRouter()

#GET
@router.get(path='/')
async def all_affinities():
    return ('res')

#POST


#PUT


#DELETE