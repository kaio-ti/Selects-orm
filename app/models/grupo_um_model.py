from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String


@dataclass
class GrupoUmModel(db.Model):
    id: int
    nome: str
    idade: int
    __tablename__='grupo_um'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)