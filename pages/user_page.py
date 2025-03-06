import json

import requests

class UserPage:
    def __init__(self):
        # url del endpoint con el que se va a trabajar
        self.base_url = "https://reqres.in/api/users"

    def crear_usuario_informacion_basica(self, name, job):
        # Se realiza el envio POST para la creacion del usuario informacion basica.
        data = {
            "name": name,
            "job": job
        }
        response = requests.post(self.base_url, json=data)
        return response

    def crear_usuario_informacion_extra(self, name, job, gender, age):
        # Se realiza el envio POST para la creacion del usuario con informacion adicional.
        data = {
            "name": name,
            "job": job,
            "gender": gender,
            "age": age
        }
        response = requests.post(self.base_url, json=data)
        return response

    def crear_usuario_informacion_no_valida(self, name, job, gender, age):
        # Se realiza el envio POST de un json mal formado para la NO creacion del usuario
        data = {
            "name": name,
            "job": job,
            "gender": gender,
            "age": age
        }
        # Convierto a un string JSON y le agrego una coma extra al final
        malformed_json = json.dumps(data) + ','
        headers = {"Content-Type": "application/json"}

        response = requests.post(self.base_url, data=malformed_json, headers=headers)
        return response