import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from schedule_service.app import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_courses_api(client):
    response = client.get('/courses')
    assert response.status_code == 200
    data = response.get_json()
    assert any(course['name'] == 'Математика' for course in data)