from datetime import datetime, timedelta
from uuid import uuid4

from pydantic import BaseModel, Field

from central.domain.model.secret import Secret


class AccessToken(BaseModel):
    token: str = Field(default_factory=lambda: Secret().secret, repr=False)
    expires: datetime

    def is_valid(self) -> bool:
        return self.expires < datetime.utcnow()

    @classmethod
    def create(cls, duration: int = 120) -> "AccessToken":
        return cls(expires=datetime.utcnow() + timedelta(seconds=duration))
