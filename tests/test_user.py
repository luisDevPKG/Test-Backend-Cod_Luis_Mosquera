import pytest

from pages.user_page import UserPage


@pytest.fixture
def user_page():
    return UserPage() # instacia de la clase que maneja las peticiones HTTP

@pytest.mark.parametrize("name, job", [
    ("Prueba00", "Prueba00"),
    ("Prueba01", "Prueba01"),
    ("Prueba02", "Prueba02")
])

# Primer caso
def test_crear_usuario_informacion_basica(user_page, name, job):
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


