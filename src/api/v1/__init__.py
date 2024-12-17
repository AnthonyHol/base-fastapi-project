"""
Directory for describing routers.

Router example:
from fastapi import APIRouter, status

router = APIRouter(prefix="/resources", tags=["Resources"])


@router.get("", status_code=status.HTTP_200_OK, response_model=SomeSchema)
async def get_resources(
    resource_service: ResourceService = Depends(),
) -> Resource:
    return await resource_service.get_all()
"""

