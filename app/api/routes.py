from fastapi import APIRouter

from app.api.endpoints import admission_request, grimories, magic_affinities

router = APIRouter()
router.include_router(admission_request.router, prefix='/request', tags=["Applications"])
router.include_router(grimories.router, prefix='/grimoire', tags=["Grimoire"])
router.include_router(magic_affinities.router, prefix='/affinities', tags=["Magic Affinities"])
