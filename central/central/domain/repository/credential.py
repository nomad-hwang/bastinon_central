import abc

from central.domain.model.credential import Credential


class CredentialRepo(abc.ABC):
    @abc.abstractmethod
    def get(self, uid: str) -> Credential | None:
        pass

    @abc.abstractmethod
    def create(self, credential: Credential, secret: str) -> None:
        pass

    @abc.abstractmethod
    def update_secret(self, credential: Credential, secret: str) -> None:
        pass


class CredentialRepoPlaceHolder(CredentialRepo):
    def get(self, uid: str) -> Credential | None:
        pass

    def create(self, credential: Credential, secret: str) -> None:
        pass

    def update_secret(self, credential: Credential, secret: str) -> None:
        pass
