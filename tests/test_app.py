from app import app

def test_home_endpoint():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200

def test_health_endpoint():
    tester = app.test_client()
    response = tester.get("/health")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "OK"