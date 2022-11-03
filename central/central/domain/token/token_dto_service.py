from datetime import datetime

from pydantic import BaseModel


class ValidateRequestDto(BaseModel):
    token: str


class DeleteRequestDto(BaseModel):
    token: str


class GenerateRequestDto(BaseModel):
    duration: int


class GenerateResponseDto(BaseModel):
    token: str
    expires_at: datetime
