import abc

from central.domain.model import Bastion, Client


class BastionRepo(abc.ABC):
    @abc.abstractmethod
    def get(self, uid: str) -> Bastion:
        pass

    @abc.abstractmethod
    def get_all(self) -> list[Bastion]:
        pass

    @abc.abstractmethod
    def get_all_clients(self) -> list[Client]:
        pass

    @abc.abstractmethod
    def get_by_client_uid(self, client_uid: str) -> Bastion:
        pass

    @abc.abstractmethod
    def create(self, bastion: Bastion) -> Bastion:
        pass

    @abc.abstractmethod
    def update(self, bastion: Bastion) -> Bastion:
        pass

    @abc.abstractmethod
    def delete(self, uid: str) -> None:
        pass


# Path: bastion_central/repository/client.py
