import logging
from contextlib import contextmanager

from sqlalchemy import create_engine, orm


class Database(object):
    _logger = logging.getLogger("uvicorn").getChild(__name__)

    def __init__(self, db_url: str):
        self._engine = create_engine(
            db_url,
            pool_pre_ping=True,
        )
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(autoflush=False, autocommit=False, bind=self._engine)
        )

    @contextmanager
    def session_context(self):
        session: orm.Session = self._session_factory()
        try:
            yield session
        except Exception:
            self._logger.exception("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()

    @property
    def engine(self):
        return self._engine
