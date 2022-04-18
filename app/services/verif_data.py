def verify_data(data):
    for key in data.keys():
        if type(data[key]) != str:
            return {"error": f" A chave {key} está em um formato inválido."}
