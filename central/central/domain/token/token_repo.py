from datetime import datetime

from central.adopter.database.model.token import TokenORM
from central.domain.token.token_entity import Token


class TokenRepo(object):
    def __init__(self, session_context):
        self._session_context = session_context

    def create(self, token: Token) -> None:
        with self._session_context() as session:
            session.add(TokenORM(**token.dict()))

    def get(self, token: str) -> Token:
        with self._session_context() as session:
            ret: TokenORM = session.query(TokenORM).filter_by(token=token).first()
            return Token(**ret.dict())

    def delete(self, token: str) -> None:
        with self._session_context() as session:
            session.query(TokenORM).filter_by(token=token).delete()

    def delete_expired(self) -> None:
        with self._session_context() as session:
            session.query(TokenORM).filter(
                TokenORM.expired_at < datetime.utcnow()
            ).delete()
