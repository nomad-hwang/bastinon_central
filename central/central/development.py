from central.adopter.database.model.base import Base
from central.container import Container


def dev_setup(container: Container) -> None:
    db = container._database()
    Base.metadata.drop_all(db.engine)
    Base.metadata.create_all(db.engine)
