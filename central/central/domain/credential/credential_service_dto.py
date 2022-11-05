from pydantic import BaseModel


class CheckReqDto(BaseModel):
    uid: str


class CreateReqDto(BaseModel):
    uid: str


class CreateRespDto(BaseModel):
    uid: str
    password: str | None = None
    error: str | None = None


class DeleteReqDto(BaseModel):
    uid: str


class UpdateReqDto(BaseModel):
    uid: str
    password: str
