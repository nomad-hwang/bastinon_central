from datetime import datetime

from pydantic import BaseModel


class ValidateAccessTokenInDto(BaseModel):
    token: str


class DeleteAccessTokenInDto(BaseModel):
    token: str


class GenerateAccessTokenInDto(BaseModel):
    duration: int


class GenerateAccessTokenOutDto(BaseModel):
    token: str
