from central.domain.token.token_dto_service import (DeleteRequestDto,
                                                    GenerateRequestDto,
                                                    GenerateResponseDto,
                                                    ValidateRequestDto)
from central.domain.token.token_entity import Token
from central.domain.token.token_repo import TokenRepo


class TokenService(object):
    def __init__(self, access_token_repo: TokenRepo):
        self._repo = access_token_repo

    def validate(self, dto: ValidateRequestDto):
        t = self._repo.get(dto.token)
        if t is None:
            raise ValueError("Invalid token")

    def generate(self, dto: GenerateRequestDto) -> GenerateResponseDto:
        token = Token.create(**dto.dict())
        self._repo.create(token)
        return GenerateResponseDto(token=token.token, expires_at=token.expires_at)

    def delete(self, dto: DeleteRequestDto) -> None:
        self._repo.delete(dto.token)

    def delete_expired(self) -> None:
        self._repo.delete_expired()
