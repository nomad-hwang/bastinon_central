from datetime import datetime, timedelta

from central.domain.dto.access_token import (DeleteAccessTokenInDto,
                                             GenerateAccessTokenInDto,
                                             GenerateAccessTokenOutDto,
                                             ValidateAccessTokenInDto)
from central.domain.model.access_token import AccessToken
from central.domain.repository.access_token import AccessTokenRepo


class AccessTokenService(object):
    def __init__(self, repo: AccessTokenRepo):
        self._repo = repo

    def validate(self, dto: ValidateAccessTokenInDto):
        t = self._repo.get_by_token(dto.token)
        if t is None:
            raise ValueError("Invalid token")

    def generate(self, dto: GenerateAccessTokenInDto) -> GenerateAccessTokenOutDto:
        t = AccessToken.create(dto.duration)
        self._repo.create(t)
        return GenerateAccessTokenOutDto(token=t.token)

    def delete(self, dto: DeleteAccessTokenInDto) -> None:
        self._repo.delete_by_token(dto.token)

    def delete_expired(self) -> None:
        self._repo.deletes([t for t in self._repo.get_all() if not t.is_valid()])
