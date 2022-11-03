from pydantic import BaseModel


class Client(BaseModel):
    uid: str
    name: str
    online: bool = False
    port_alloc: int = None
