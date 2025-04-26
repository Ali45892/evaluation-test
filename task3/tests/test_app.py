import pytest
from app import app as flask_app

@pytest.fixture
def app():
    return flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_route(client):
    """Test that the home route returns a response"""
    response = client.get('/')
    assert response.status_code == 200
