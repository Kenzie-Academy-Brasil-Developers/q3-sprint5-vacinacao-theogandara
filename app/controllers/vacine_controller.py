from flask import current_app, jsonify, request, session
from app.models.vacine_model import Vacine


def get_vacines():
    vacines = Vacine.query.all()

    serialized = [
        {
            "cpf": vacine.cpf,
            "name": vacine.name,
            "vaccine_name": vacine.vaccine_name,
            "health_unit_name": vacine.health_unit_name,
        }
        for vacine in vacines
    ]

    return jsonify(serialized), 200


def create_vacine():
    data = request.get_json()

    new_vaccine = Vacine(**data)

    session = current_app.db.session

    session.add(new_vaccine)
    session.commit()

    print(new_vaccine)

    return "", 201
