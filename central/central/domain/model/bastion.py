from threading import Lock

from pydantic import BaseModel

_GLOBAL_LOCK: dict[str, Lock] = {}


class Bastion(BaseModel):
    uid: str
    name: str
    host: str
    port: int
    online: bool = False
    port_alloc: dict[str, int] = {}
    port_alloc_cnt: int = 0
    open_port_sta: int = 10000
    open_port_end: int = 20000

    # on init, create a lock for this bastion
    def __init__(self, **data):
        super().__init__(**data)
        _GLOBAL_LOCK[self.uid] = Lock()

    def acquire_port(self, client_uid: str) -> int:
        """Allocate a port for the user"""
        with self._lock:
            if self.port_alloc_cnt >= self.open_port_end - self.open_port_sta:
                raise Exception("No more ports available")
            if client_uid in self.port_alloc:
                raise Exception(f"Client {client_uid} already has a port acquired")
            available_ports = set(range(self.open_port_sta, self.open_port_end))
            allocated_ports = set(self.port_alloc.values())
            available_ports = available_ports - allocated_ports
            return available_ports.pop()

    def release_port(self, username: str) -> None:
        """Release the port for the user"""
        with self._lock:
            if username not in self.port_alloc:
                raise Exception(f"Port not allocated for {username}")
            del self.port_alloc[username]
