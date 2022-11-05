import abc
from enum import Enum

from central.domain.credential.credential_repo_dto import (
    RepoCreateReqDto,
    RepoCreateRespDto,
    RepoGetReqDto,
    RepoGetRespDto,
    RepoUpdateReqDto,
)


class CredentialRepo(abc.ABC):
    @abc.abstractmethod
    def create(self, dto: RepoCreateReqDto) -> RepoCreateRespDto:
        pass

    @abc.abstractmethod
    def get(self, dto: RepoGetReqDto) -> RepoGetRespDto:
        pass

    @abc.abstractmethod
    def update(self, dto: RepoUpdateReqDto) -> None:
        pass

    @abc.abstractmethod
    def delete(self, dto: RepoGetReqDto) -> None:
        pass
