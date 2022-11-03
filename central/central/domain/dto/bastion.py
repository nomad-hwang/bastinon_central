from pydantic import BaseModel

from central.domain.model.bastion import Bastion


class AddInDto(BaseModel):
    uid: str
    name: str
    host: str
    port: int

    def to_domain(self) -> Bastion:
        return Bastion(
            uid=self.uid,
            name=self.name,
            host=self.host,
            port=self.port,
        )


class UpdateInDto(BaseModel):
    uid: str
    name: str | None = None
    host: str | None = None
    port: int | None = None
    online: bool | None = None
    open_port_sta: int | None = None
    open_port_end: int | None = None

    def to_domain(self, original: Bastion) -> Bastion:
        copy = original.copy(deep=True)
        if self.uid != copy.uid:
            raise Exception("UID cannot be changed")
        copy.name = self.name or copy.name
        copy.host = self.host or copy.host
        copy.port = self.port or copy.port
        copy.online = self.online or copy.online
        copy.open_port_sta = self.open_port_sta or copy.open_port_sta
        copy.open_port_end = self.open_port_end or copy.open_port_end
        if copy.open_port_sta > copy.open_port_end:
            raise Exception(
                f"Invalid port range: start={copy.open_port_sta}, end={copy.open_port_end}"
            )
        return copy


class DeleteInDto(BaseModel):
    uid: str


class GetInDto(BaseModel):
    uid: str
