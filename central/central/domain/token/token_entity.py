from datetime import datetime, timedelta
from uuid import uuid4

from pydantic import BaseModel, Field


class Token(BaseModel):
    token: str = Field(default_factory=lambda: str(uuid4()) + "-" + str(uuid4()))
    expires_at: datetime
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def is_valid(self) -> bool:
        return self.expires_at < datetime.utcnow()

    @classmethod
    def create(cls, duration: int) -> "Token":
        return cls(expires_at=datetime.utcnow() + timedelta(seconds=duration))
