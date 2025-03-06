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
