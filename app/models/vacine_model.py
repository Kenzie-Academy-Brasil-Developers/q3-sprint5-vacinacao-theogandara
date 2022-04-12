from sqlalchemy import Column, DateTime, String
from app.configs.database import db

class Vacine(db.Model):
    __tablename__ = "vaccine_cards"

    cpf = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    first_shot_date = Column(DateTime)
    second_shot_date = Column(DateTime)
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String)