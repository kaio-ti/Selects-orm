from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import backref, relationship


@dataclass
class GrupoDoisModel(db.Model):
    id: int
    nome: str
    idade: int
    __tablename__='grupo_dois'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    conjuge_id = Column(Integer, ForeignKey("grupo_um.id"), nullable=False, unique=True)
    conjuge = relationship("GrupoUmModel", backref=backref("conjuge", uselist=False), uselist=False)