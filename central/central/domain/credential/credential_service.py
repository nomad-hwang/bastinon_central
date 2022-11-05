from central.domain.credential.credential_entity import Credential
from central.domain.credential.credential_repo import CredentialRepo
from central.domain.credential.credential_repo_dto import (
    RepoCreateReqDto,
    RepoGetReqDto,
)
from central.domain.credential.credential_service_dto import (
    CheckReqDto,
    CreateReqDto,
    CreateRespDto,
    UpdateReqDto,
)


class CredentialService(object):
    def __init__(self, credential_repo: CredentialRepo):
        self._repo = credential_repo

    def check_exists(self, dto: CheckReqDto) -> tuple[bool, str | None]:
        user = self._repo.get(RepoGetReqDto(uid=dto.uid))
        if user.error is not None:
            return False, user.error
        return True, None

    def create(self, dto: CreateReqDto) -> CreateRespDto:
        password = Credential.generate_password()
        ret = self._repo.create(RepoCreateReqDto(uid=dto.uid, password=password))
        return CreateRespDto(uid=dto.uid, password=password, error=ret.error)

    def update(self, dto: UpdateReqDto) -> None:
        raise NotImplementedError
