from sqlalchemy import Column, DateTime, String
from app.configs.database import db
from sqlalchemy.orm import validates
from dataclasses import dataclass
from app.exc.errors import CpfInvalid


@dataclass
class Vacine(db.Model):

    cpf = str
    name = str
    first_shot_date = DateTime
    second_shot_date = DateTime
    vaccine_name = str
    health_unit_name = str

    __tablename__ = "vaccine_cards"

    cpf = Column(String(11), primary_key=True)
    name = Column(String, nullable=False)
    first_shot_date = Column(DateTime)
    second_shot_date = Column(DateTime)
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String)

    @validates("cpf")
    def validate_cpf(self, key, cpf_to_be_tested):
        if len(cpf_to_be_tested) != 11:
            raise CpfInvalid

        return cpf_to_be_tested
