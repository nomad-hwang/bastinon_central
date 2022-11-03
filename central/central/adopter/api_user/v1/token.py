from dependency_injector.providers import Configuration
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from central.adopter.api_user.v1.model.token import GenerateTokenResponse
from central.container import Container
from central.domain.dto.access_token import GenerateAccessTokenInDto
from central.domain.service.access_token import AccessTokenService

router = APIRouter()


@router.post("", status_code=201, response_model=GenerateTokenResponse)
@inject
def register(
    token: AccessTokenService = Depends(Provide[Container.access_token_service]),
    config: Configuration = Depends(Provide[Container.config]),
):
    return GenerateTokenResponse.of(
        token.generate(
            GenerateAccessTokenInDto(duration=config.credential.token_duration)
        )
    )
