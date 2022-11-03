from uuid import uuid4

from pydantic import BaseModel, Field


class Credential(BaseModel):
    uid: str

    @staticmethod
    def generate_password() -> str:
        return str(uuid4()) + "-" + str(uuid4())
