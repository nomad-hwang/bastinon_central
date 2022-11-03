from datetime import datetime

from pydantic import BaseModel

from central.domain.model.credential import Credential


class CheckCrednetialExistsInDto(BaseModel):
    uid: str


class CreateCredentialInDto(BaseModel):
    uid: str

    def to_domain(self) -> Credential:
        return Credential(uid=self.uid)


class CreateCredentialOutDto(BaseModel):
    uid: str
    secret: str


class DeleteCredentialsInDto(BaseModel):
    uid: str


class NewCredentialSecretInDto(BaseModel):
    uid: str


class NewCredentialSecretOutDto(BaseModel):
    uid: str
    secret: str
