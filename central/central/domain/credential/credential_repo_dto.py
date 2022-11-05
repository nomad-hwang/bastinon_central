from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class RepoCreateReqDto(BaseModel):
    uid: str
    password: str


class RepoCreateRespDto(BaseModel):
    uid: str
    error: str | None


class RepoGetReqDto(BaseModel):
    uid: str


class RepoGetRespDto(BaseModel):
    uid: str
    password: str | None = None
    error: str | None = None


class RepoUpdateReqDto(BaseModel):
    uid: str
    password: str


class RepoDeleteRequestDto(BaseModel):
    uid: str
