import pytest

from pages.user_page import UserPage


class TestUser:

    @pytest.fixture
    def user_page(self):
        return UserPage() # instacia de la clase que maneja las peticiones HTTP


    @pytest.mark.parametrize("name, job", [
        ("Prueba00", "Prueba00"),
        ("Prueba01", "Prueba01"),
        ("Prueba02", "Prueba02")
    ])
    # Primer caso
    def test_crear_usuario_informacion_basica(self,user_page, name, job):
        # Crear un nuevo usuario
        response = user_page.crear_usuario_informacion_basica(name, job)

        # Imprime la respuesta en consola
        print("\nResponse Status Code:", response.status_code)
        print("Response JSON:", response.json())

        # Verificar que el codigo de estado sea 201
        assert response.status_code == 201, f"La solicitud fallo, se obtiene el código {response.status_code}"

        # Verificar la existencia de los campos esperados en la respuesta
        user_data = response.json()
        expected_fields = ["name", "job", "id", "createdAt"]
        for field in expected_fields:
            assert field in user_data, f"Fallo: Informacion incompleta, falta el campo {field} en la respuesta"

        assert user_data["name"] == name, "El campo 'name' no coincide"
        assert user_data["job"] == job, "El campo 'job' no coincide"


    @pytest.mark.parametrize("name, job, gender, age", [
        ("Prueba001", "Prueba001", "Female", 25),
        ("Prueba002", "Prueba002", "Male", 32),
        ("Prueba003", "Prueba003", "Female", 28)
    ])
    # Segundo caso
    def test_crear_usuario_informacion_adicional(self,user_page, name, job, gender, age):
        # Crear usuario con campos adicionales
        response = user_page.crear_usuario_informacion_extra(name, job, gender, age)

        # Imprime la respuesta en consola
        print("\nResponse Status Code:", response.status_code)
        print("Response JSON:", response.json())

        # Verificar que el codigo de estado sea 201
        assert response.status_code == 201, f"La solicitud falló, se obtiene el código{response.status_code}"

        # Verificar los campos esperados en la respuesta
        user_data = response.json()
        expected_fields = ["name", "job", "gender", "age", "id", "createdAt"]
        for field in expected_fields:
            assert field in user_data, f"Fallo: Informacion incompleta, falta el campo {field} en la respuesta"

        assert user_data["name"] == name, "La prueba fallo, la infomacion del campo 'name' no coincide"
        assert user_data["job"] == job, "La prueba fallo, la infomacion del campo 'job' no coincide"
        assert user_data["gender"] == gender, "La prueba fallo, la infomacion del campo 'gender' no coincide"
        assert isinstance(user_data["age"], int), "La prueba fallo, la infomacion del campo 'age' no es un entero"


    @pytest.mark.parametrize("name, job, gender, age", [
        ("Prueba001", "Prueba001", "Female", 25),
        ("Prueba002", "Prueba002", "Male", 32),
        ("Prueba003", "Prueba003", "Female", 28)
    ])
    # Tercer caso
    def test_crear_usuario_repetido(self, user_page, name, job, gender, age):
        # Enviar una peticion POST con un json mal formado y esperar un 400
        response = user_page.crear_usuario_informacion_no_valida(name, job, gender, age)

        # Verifica el tipo de contenido de la respuesta
        content_type = response.headers.get('Content-Type', '')
        print("Content-Type:", content_type)

        # Imprimo el JSON de respuesta, si está disponible, sino capturo la excepcion e imprimo la respuesta
        try:
            response_json = response.json()
            print("Response JSON:", response_json)
        except ValueError:
            print("La respuesta no es un JSON válido. Contenido de la respuesta es:")
            print(response.text)  # Imprimo el HTML o el contenido de error que retorna el servidor

        # Verificar código de estado 400
        assert response.status_code == 400, f"Se esperaba un 400, pero se recibió {response.status_code}"
