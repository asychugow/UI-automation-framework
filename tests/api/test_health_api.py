from api.endpoints import Endpoints

class TestHealth:

    def test_health_status(api_client):
        response = api_client.get(Endpoints.HEALTH)
        body = response.json()

        assert response.status_code == 200
        assert body["success"] == True
        assert body["message"] == "Notes API is Running"