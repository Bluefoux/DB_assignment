from datetime import date
from typing import Optional

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import (DeclarativeBase, Mapped, MappedAsDataclass,
                            mapped_column)

class Base(MappedAsDataclass, DeclarativeBase):
    """subclasses will be converted to dataclasses"""
    pass


db = SQLAlchemy(model_class=Base)


class competitions(db.Model):
    __tablename__ = "competitions"

    comp_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    comp_name: Mapped[str] = mapped_column(String(255), unique=True)
    compdate: Mapped[date] = mapped_column(init=False)
    compvenue: Mapped[str] = mapped_column(String(255))

    def __repr__(self):
        return f"{self.comp_id}, {self.comp_name}"


class events(db.Model):
    __tablename__ = "events"

    event_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    event_name: Mapped[str] = mapped_column(String(255), unique=True)
    distance: Mapped[int]
    gender: Mapped[str] = mapped_column(String(6))
    maxAge: Mapped[int]
    qualifyingTime: Mapped[Optional[int]]
    isRelay: Mapped[bool]
    comp_id: Mapped[int] = mapped_column(ForeignKey("competitions.comp_id"))

    def __repr__(self):
        return f"{self.event_id}, {self.event_name}"