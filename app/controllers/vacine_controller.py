from http import HTTPStatus
from flask import current_app, jsonify, request
from app.models.vacine_model import Vacine
from sqlalchemy.exc import IntegrityError
from app.exc.errors import CpfInvalid
from app.services.verif_data import verify_data
from app.services.generate_data import data_generate


def get_vacines():
    vacines = Vacine.query.all()

    serialized = [
        {
            "cpf": vacine.cpf,
            "name": vacine.name,
            "vaccine_name": vacine.vaccine_name,
            "health_unit_name": vacine.health_unit_name,
            "first_shot_date": vacine.first_shot_date,
            "second_shot_date": vacine.second_shot_date
        }
        for vacine in vacines
    ]

    return jsonify(serialized), 200


def create_vacine():
    data = request.get_json()

    verify_data(data)

    for key in data.keys():
        if type(data[key]) != str:
            return {"error": f" A chave {key} está em um formato inválido."}

    try:
        new_vaccine = Vacine(
            cpf=data["cpf"],
            name=data["name"],
            vaccine_name=data["vaccine_name"],
            health_unit_name=data["health_unit_name"],
            first_shot_date=data_generate(),
            second_shot_date=data_generate()
        )

        session = current_app.db.session

        session.add(new_vaccine)
        session.commit()

        return jsonify(new_vaccine), 201

    except IntegrityError:
        return {"message": "CPF já cadastrado."}, HTTPStatus.CONFLICT

    except CpfInvalid:
        return {"message": "O CPF não está no formato correto."}, HTTPStatus.BAD_REQUEST

    except KeyError as err:
        return {"message": f"Está faltando a Key {str(err)}."}, HTTPStatus.BAD_REQUEST


    
