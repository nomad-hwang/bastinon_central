from datetime import datetime

from pydantic import BaseModel

from central.domain.credential.credential_entity import Credential


class CheckExistsRequestDto(BaseModel):
    uid: str


class CreateRequestDto(BaseModel):
    uid: str


class CreateResponseDto(BaseModel):
    uid: str
    password: str  # response only on create


class DeleteRequestDto(BaseModel):
    uid: str


class UpdateRequestDto(BaseModel):
    uid: str
    password: str
