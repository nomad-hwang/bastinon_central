import abc

from central.domain.model import Bastion, Client


class ClientRepo(abc.ABC):
    @abc.abstractmethod
    def get(self, uid: str) -> Bastion:
        pass

    @abc.abstractmethod
    def get_all(self) -> list[Bastion]:
        pass

    @abc.abstractmethod
    def get_by_bastion_uid(self, bastion_uid: str) -> Client:
        pass

    @abc.abstractmethod
    def create(self, client: Client) -> Client:
        pass

    @abc.abstractmethod
    def update(self, client: Client) -> Client:
        pass

    @abc.abstractmethod
    def delete(self, uid: str) -> None:
        pass
