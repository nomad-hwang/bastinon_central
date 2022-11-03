import abc

from central.domain.model.access_token import AccessToken


class AccessTokenRepo(abc.ABC):
    @abc.abstractmethod
    def get_by_token(self, token: str) -> AccessToken | None:
        pass

    @abc.abstractmethod
    def get_all(self) -> list[AccessToken]:
        pass

    @abc.abstractmethod
    def create(self, token: AccessToken) -> None:
        pass

    @abc.abstractmethod
    def update(self, token: AccessToken) -> None:
        pass

    @abc.abstractmethod
    def delete_by_token(self, token: str) -> None:
        pass

    @abc.abstractmethod
    def deletes(self, tokens: list[AccessToken]) -> None:
        pass


class AccessTokenRepoPlaceHolder(AccessTokenRepo):  # TODO: Remove this class
    def get_by_token(self, token: str) -> AccessToken | None:
        pass

    def create(self, token: AccessToken) -> None:
        pass

    def delete_by_token(self, token: AccessToken) -> None:
        pass
