from pydantic import BaseModel


class LDAPClientCredential(BaseModel):
    username: str
    password: str | None = None
