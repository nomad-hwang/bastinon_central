from threading import Lock

from central.domain.dto.bastion import AddInDto, UpdateInDto
from central.domain.model import Bastion
from central.domain.repository import BastionRepo

# from bastion_central.service.bastion_facade import BastionFacade

_GLOBAL_LOCK: dict[str, Lock] = {}


class BastionService(object):
    def __init__(self, bastion_repo: BastionRepo):
        self._repo = bastion_repo

    def add(self, dto: AddInDto) -> None:
        self._repo.create(dto.to_domain())

    def update(self, dto: UpdateInDto) -> None:
        if dto.uid not in _GLOBAL_LOCK:
            _GLOBAL_LOCK[dto.uid] = Lock()
        with _GLOBAL_LOCK[dto.uid]:
            self._repo.update(dto.to_domain(self._repo.get(dto.uid)))

    def get(self, uid: str) -> Bastion | None:
        return self._repo.get(uid)

    def delete(self, uid: str) -> None:
        self._repo.delete(uid)

    def get_all(self) -> list[Bastion]:
        return self._repo.get_all()

    def transfer_clients(self, dto) -> None:
        raise NotImplementedError()
