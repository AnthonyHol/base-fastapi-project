"""
File for describing general routers.

Router import example:
from api.v1.resource import router as resource_router

v1_router.include_router(resource_router)
"""
from fastapi import APIRouter

v1_router = APIRouter(prefix="/v1")

api_router = APIRouter(prefix="/api")
api_router.include_router(v1_router)
