from dependency_injector.providers import Configuration
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from central.adopter.api.v1.model.token import GenerateResponse
from central.container import Container
from central.domain.token.token_dto_service import GenerateRequestDto
from central.domain.token.token_service import TokenService

router = APIRouter()


"""  
Note:   Token is used to provision a client.
        
        Process of provisioning a client:
        
        1. Requests a token from the server. (This is done by the user)
        2. User sends/type in the token to the client.
        3. Client sends the token to the server for registration.
        4. Server validates the token and creates a credential(including random password) for the client.
        5. Server returns the credential to the client. (Only time the password is returned)
        6. Client stores the credential.
        7. Client uses the credential to authenticate to the server.        
"""


@router.get("", status_code=status.HTTP_201_CREATED, response_model=GenerateResponse)
@inject
def get_token(
    token: TokenService = Depends(Provide[Container.access_token_service]),
    config: Configuration = Depends(Provide[Container.config]),
):
    duration = config["credential"]["token_duration"] or 600  # default 10 minutes
    ret = token.generate(GenerateRequestDto(duration=duration))  # type: ignore
    return GenerateResponse(**ret.dict())
