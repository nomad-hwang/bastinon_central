from pydantic import BaseModel

from central.domain.dto.access_token import ValidateAccessTokenInDto
from central.domain.dto.credentials import (CreateCredentialInDto,
                                            CreateCredentialOutDto)


class GetAccessTokenRequest(BaseModel):
    uid: str
    secret: str

    def to_credential_dto(self) -> CreateCredentialInDto:
        return CreateCredentialInDto(uid=self.uid)


class GetAccessTokenResponse(BaseModel):
    access_token: str

    @classmethod
    def of(cls, dto: ValidateAccessTokenInDto) -> "GetAccessTokenResponse":
        return cls(access_token=dto.token)
