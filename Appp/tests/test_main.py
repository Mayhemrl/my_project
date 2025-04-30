from main_service.app import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_main_page(client):
    response = client.get('/')
    assert response.status_code == 200
    # Используем декодированный текст вместо байтов
    assert "Интернет-магазин" in response.get_data(as_text=True)