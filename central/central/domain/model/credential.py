from datetime import datetime

from pydantic import BaseModel


class Credential(BaseModel):
    uid: str
