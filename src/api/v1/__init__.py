"""
Directory for describing routers.

Router example:
from typing import Annotated

from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/resources", tags=["Resources"])


@router.get("", status_code=status.HTTP_200_OK, response_model=SomeSchema)
async def get_resources(
    resource_service: Annotated[ResourceService, Depends()],
) -> Resource:
    return await resource_service.get_all()
"""
