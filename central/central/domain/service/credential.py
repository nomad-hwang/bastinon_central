from central.domain.dto.credentials import (CheckCrednetialExistsInDto,
                                            CreateCredentialInDto,
                                            CreateCredentialOutDto,
                                            NewCredentialSecretInDto,
                                            NewCredentialSecretOutDto)
from central.domain.model.secret import Secret
from central.domain.repository.credential import CredentialRepo


class CredentialService(object):
    def __init__(self, credential_repo: CredentialRepo):
        self._repo = credential_repo

    def check_exists(self, dto: CheckCrednetialExistsInDto) -> None:
        if self._repo.get(dto.uid) is None:
            raise ValueError(f"credential {dto.uid} not found")

    def create(self, dto: CreateCredentialInDto) -> CreateCredentialOutDto:
        secret = Secret().secret
        self._repo.create(dto.to_domain(), secret)
        return CreateCredentialOutDto(uid=dto.uid, secret=secret)

    def update(self, dto: NewCredentialSecretInDto) -> NewCredentialSecretOutDto:
        raise NotImplementedError()
