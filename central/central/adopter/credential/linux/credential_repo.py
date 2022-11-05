from central.adopter.credential.linux.credential_repo_facade import (
    LinuxCredentialFacade,
)
from central.domain.credential.credential_repo import CredentialRepo
from central.domain.credential.credential_repo_dto import (
    RepoCreateReqDto,
    RepoCreateRespDto,
    RepoDeleteRequestDto,
    RepoGetReqDto,
    RepoGetRespDto,
    RepoUpdateReqDto,
)

""" 
TODO: Consider using libuser to manage. https://pagure.io/libuser
"""


class LinuxCredentialRepo(CredentialRepo, LinuxCredentialFacade):
    def create(self, dto: RepoCreateReqDto) -> RepoCreateRespDto:
        if err := self._create_user(dto.uid, dto.password):
            return RepoCreateRespDto(uid=dto.uid, error=err)
        return RepoCreateRespDto(uid=dto.uid, error=None)

    def get(self, dto: RepoGetReqDto) -> RepoGetRespDto:
        password, error = self._get_user(dto.uid)
        return RepoGetRespDto(
            uid=dto.uid,
            password=password,
            error=error,
        )

    def update(self, dto: RepoUpdateReqDto) -> None:
        raise NotImplementedError

    def delete(self, dto: RepoDeleteRequestDto) -> None:
        raise NotImplementedError
