from uuid import uuid4

from pydantic import BaseModel, Field


class Secret(BaseModel):
    secret: str = Field(
        default_factory=lambda: (str(uuid4()) + str(uuid4())), repr=False
    )
