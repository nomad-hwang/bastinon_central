from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        orm)
from sqlalchemy.ext.declarative import declarative_base

ORMBase = declarative_base()


class BastionORM(ORMBase):
    __tablename__ = "bastion"

    uid = Column(String(50), primary_key=True)
    endpoint = Column(String(50))
    endpoint_port = Column(Integer)
    exposed_port_start = Column(Integer)
    exposed_port_end = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    sessions = orm.relationship("SessionORM", back_populates="bastion")


class ClientORM(ORMBase):
    __tablename__ = "client"

    uid = Column(String(50), primary_key=True)
    # TODO: hash later. maybe should develop custom PAM module to authenticate with hashed password
    password = Column(String(50))

    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    sessions = orm.relationship("SessionORM", back_populates="client")


class SessionORM(ORMBase):
    __tablename__ = "session"

    uid = Column(String(50), primary_key=True)
    bastion_uid = Column(String(50), ForeignKey("bastion.uid"))
    client_uid = Column(String(50), ForeignKey("client.uid"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    closed_at = Column(DateTime)
    closed = Column(Boolean)

    bastion = orm.relationship("BastionORM", back_populates="sessions")
    client = orm.relationship("ClientORM", back_populates="sessions")


class AuditLogORM(ORMBase):
    __tablename__ = "audit_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    level = Column(String(50), nullable=False)
    message = Column(String(1000), nullable=False)
    created_at = Column(DateTime)
    audited_by = Column(String(50))

    client_uid = Column(String(50), ForeignKey("client.uid"), nullable=True)
    client = orm.relationship(
        "ClientORM", back_populates="audit_logs", uselist=False
    )  # One client per audit log

    bastion_uid = Column(String(50), ForeignKey("bastion.uid"), nullable=True)
    bastion = orm.relationship(
        "BastionORM", back_populates="audit_logs", uselist=False
    )  # One bastion per audit log
