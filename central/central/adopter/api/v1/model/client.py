from pydantic import BaseModel


class ClientRegisterReq(BaseModel):
    uid: str
    token: str


class ClientRegisterResp(BaseModel):
    uid: str
    password: str
    message: str
