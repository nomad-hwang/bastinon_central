from datetime import datetime

from pydantic import BaseModel


class GenerateResponse(BaseModel):
    token: str
    expires_at: datetime
