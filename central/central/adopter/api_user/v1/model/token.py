from pydantic import BaseModel

from central.domain.dto.access_token import GenerateAccessTokenOutDto


class GenerateTokenResponse(BaseModel):
    token: str

    @classmethod
    def of(cls, dto: GenerateAccessTokenOutDto) -> "GenerateTokenResponse":
        return cls(token=dto.token)
