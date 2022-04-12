from flask import Blueprint
from app.controllers.vacine_controller import get_vacines, create_vacine

bp = Blueprint("vacine_bp", __name__, url_prefix="/vaccinations")

bp.post('')(create_vacine)
bp.get('')(get_vacines)