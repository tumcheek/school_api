from app import app


client = app.test_client()

def test_non_existent_index():
    response = client.get('/')
    assert response.status_code == 404