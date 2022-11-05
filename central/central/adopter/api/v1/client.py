from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException

from central.adopter.api.v1.model.client import ClientRegisterReq, ClientRegisterResp
from central.container import Container
from central.domain.credential.credential_service import CredentialService
from central.domain.credential.credential_service_dto import CreateReqDto
from central.domain.token.token_service import TokenService
from central.domain.token.token_service_dto import ValidateReqDto

router = APIRouter()


"""
TODO:   Currently, token is generated inside the cred.create() method.
TODO:   Maybe I should make secret generation service to make it more explicit and pluggable.
        secret_gen = Provide[Container.secret_generator] <- something like this
        secret_gen.generate_token()
"""


@router.post("/register", status_code=201, response_model=ClientRegisterResp)
@inject
def register_client(
    request: ClientRegisterReq,
    token: TokenService = Depends(Provide[Container.access_token_service]),
    creds: CredentialService = Depends(Provide[Container.credential_service]),
):
    if token.is_valid(ValidateReqDto(token=request.token)) is False:
        raise HTTPException(status_code=401, detail="Invalid token")

    ret = creds.create(CreateReqDto(**request.dict()))
    if ret.error:
        raise HTTPException(status_code=400, detail=ret.error)

    return ClientRegisterResp(**ret.dict(), message="Client registered successfully")
