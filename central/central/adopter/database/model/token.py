from sqlalchemy import Column, String

from central.adopter.database.model.base import Base, BaseDictMixin


class TokenORM(Base, BaseDictMixin):
    __tablename__ = "access_token"

    token = Column(String(100), nullable=False, primary_key=True)
    expires_at = Column(String(100), nullable=False)

    created_at = Column(String(100), nullable=False)
    updated_at = Column(String(100), nullable=False)

    def __repr__(self):
        return f"AccessTokenORM(token={self.token}, expires_at={self.expires_at})"
