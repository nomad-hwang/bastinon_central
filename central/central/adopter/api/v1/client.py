from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from central.adopter.api.v1.model.client import (ClientRegisterRequest,
                                                 ClientRegisterResponse)
from central.container import Container
from central.domain.credential.credential_dto_service import CreateRequestDto
from central.domain.credential.credential_service import CredentialService
from central.domain.token.token_dto_service import ValidateRequestDto
from central.domain.token.token_service import TokenService

router = APIRouter()


"""
    TODO:   Currently, token is generated inside the cred.create() method.
    TODO:   Maybe I should make secret generation service to make it more explicit and pluggable.
            secret_gen = Provide[Container.secret_generator] <- something like this
            secret_gen.generate_token()
    """


@router.post("/register", status_code=201, response_model=ClientRegisterResponse)
@inject
def register_client(
    request: ClientRegisterRequest,
    token: TokenService = Depends(Provide[Container.access_token_service]),
    creds: CredentialService = Depends(Provide[Container.credential_service]),
):
    token.is_valid(ValidateRequestDto(token=request.token))
    ret = creds.create(CreateRequestDto(uid=request.uid))
    return ClientRegisterResponse(password=ret.password)
