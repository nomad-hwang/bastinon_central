from central.domain.token.token_entity import Token
from central.domain.token.token_repo import TokenRepo
from central.domain.token.token_service_dto import (
    DeleteRequestDto,
    GenerateRequestDto,
    GenerateResponseDto,
    ValidateReqDto,
)


class TokenService(object):
    def __init__(self, access_token_repo: TokenRepo):
        self._repo = access_token_repo

    def is_valid(self, dto: ValidateReqDto) -> bool:
        if (token := self._repo.get(dto.token)) is None:
            return False
        if token.is_expired():
            return False
        self._repo.delete(token.token)  # One-time token!
        return True

    def generate(self, dto: GenerateRequestDto) -> GenerateResponseDto:
        token = Token.create(**dto.dict())
        # TODO: Hash token
        self._repo.create(token)
        return GenerateResponseDto(token=token.token, expires_at=token.expires_at)

    def delete(self, dto: DeleteRequestDto) -> None:
        self._repo.delete(dto.token)

    def delete_expired(self) -> None:
        self._repo.delete_expired()
