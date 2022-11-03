from pydantic import BaseModel

from central.domain.dto.access_token import ValidateAccessTokenInDto
from central.domain.dto.credentials import (CreateCredentialInDto,
                                            CreateCredentialOutDto)


class RegisterRequest(BaseModel):
    uid: str
    access_token: str

    def to_token_dto(self) -> ValidateAccessTokenInDto:
        return ValidateAccessTokenInDto(token=self.access_token)

    def to_credential_dto(self) -> CreateCredentialInDto:
        return CreateCredentialInDto(uid=self.uid)


class RegisterResponse(BaseModel):
    uid: str
    secret: str

    @classmethod
    def of(cls, dto: CreateCredentialOutDto) -> "RegisterResponse":
        return cls(uid=dto.uid, secret=dto.secret)
