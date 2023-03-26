from fastapi import APIRouter
from app.api.endpoints import admission_request, grimories, magic_affinities


router = APIRouter()
router.include_router(admission_request.router, prefix='/aplications', tags=["Applications"])
router.include_router(grimories.router, prefix='/grimories', tags=["Grimories"])
router.include_router(magic_affinities.router, prefix='/affinities', tags=["Magic Affinities"])