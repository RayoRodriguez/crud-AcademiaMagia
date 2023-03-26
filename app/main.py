from fastapi import FastAPI
from app.api.routes import router as api_router


app = FastAPI(
    title="Registro a la academia de magia  <IA Interactive>",
    description="API",
    version="1.0.0")


app.include_router(api_router)