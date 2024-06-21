from fastapi import FastAPI
from src.routers import router

#ads
app = FastAPI()
app.include_router(router=router, prefix="/api/v1")

