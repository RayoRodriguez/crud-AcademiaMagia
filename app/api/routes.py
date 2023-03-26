from fastapi import APIRouter
from app.api.endpoints import applications


router = APIRouter()
router.include_router(applications.router, prefix='/aplications', tags=["Applications"])