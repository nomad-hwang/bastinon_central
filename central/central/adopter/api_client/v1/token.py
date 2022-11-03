from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from central.adopter.api_client.v1.model.register import (RegisterRequest,
                                                          RegisterResponse)
from central.container import Container
from central.domain.service.access_token import AccessTokenService

router = APIRouter()


@router.post("", status_code=201, response_model=RegisterResponse)
@inject
def register(
    request: RegisterRequest,
    token: AccessTokenService = Depends(Provide[Container.access_token_service]),
):
    token.validate(request.to_token_dto())
    return RegisterResponse.of(creds.create(request.to_credential_dto()))
