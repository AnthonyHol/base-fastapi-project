"""
File for describing general routers.

Routers example:
from fastapi import APIRouter
from api.v1.resource import router as resorce_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(resource_router)

api_router = APIRouter(prefix="/api")
api_router.include_router(v1_router)
"""
