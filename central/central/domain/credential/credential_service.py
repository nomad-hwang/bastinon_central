from central.domain.credential.credential_dto_service import (
    CheckExistsRequestDto, CreateRequestDto, CreateResponseDto,
    UpdateRequestDto)
from central.domain.credential.credential_entity import Credential
from central.domain.credential.credential_repo import CredentialRepo


class CredentialService(object):
    def __init__(self, credential_repo: CredentialRepo):
        self._repo = credential_repo

    def check_exists(self, dto: CheckExistsRequestDto) -> None:
        if self._repo.get(dto.uid) is None:
            raise ValueError(f"credential {dto.uid} not found")

    def create(self, dto: CreateRequestDto) -> CreateResponseDto:
        cred = Credential(uid=dto.uid)
        self._repo.create(cred, Credential.generate_password())
        return CreateResponseDto(**cred.dict())

    def update(self, dto: UpdateRequestDto) -> None:
        self._repo.update(Credential(uid=dto.uid), dto.password)
