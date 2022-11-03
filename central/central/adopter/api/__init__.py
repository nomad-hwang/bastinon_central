from fastapi import APIRouter

from central.adopter.api.v1.client import router as client_router
from central.adopter.api.v1.token import router as token_router

api_router = APIRouter()
api_router.include_router(client_router, prefix="/api/v1/client", tags=["Client"])
api_router.include_router(token_router, prefix="/token", tags=["Token"])
