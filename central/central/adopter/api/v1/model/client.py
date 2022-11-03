from pydantic import BaseModel


class ClientRegisterRequest(BaseModel):
    uid: str
    token: str


class ClientRegisterResponse(BaseModel):
    password: str
