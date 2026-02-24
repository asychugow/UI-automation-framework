import pytest
import random
from api.endpoints import Endpoints


class TestUsers:

    def test_register_user(self, api_client):
        payload = {
            "name": f"TestUser{random.randint(1,900)}",
            "email": f"testuser{random.randint(1,900)}@example.com",
            "password": "TestPassword123"
        }
        response = api_client.post(Endpoints.REGISTER, json=payload)
        body = response.json()

        assert response.status_code == 201
        assert body["message"] == "User account created successfully"
        

    def test_login(self, api_client):
        payload = {
            "email": "testuser23@example.com",
            "password": "TestPassword123"
        }
        response = api_client.post(Endpoints.LOGIN, json=payload)

        assert response.status_code == 200
        assert "token" in response.json()["data"]

    def test_invalid_login(self, api_client):
        payload = {
            "email": "testuser@example.com",
            "password": "TestPassword123"
        }
        login = api_client.post(Endpoints.LOGIN, json=payload)
        body = login.json()

        assert login.status_code == 401
        assert body["message"] == "Incorrect email address or password"

    def test_get_profile(self, api_client):
        payload = {
            "email": "testuser23@example.com",
            "password": "TestPassword123"
        }
        login = api_client.post(Endpoints.LOGIN, json=payload)

        assert login.status_code == 200
        token = login.json()["data"]["token"]
        assert token is not None
    
        headers = {"x-auth-token": token}
        response = api_client.get(Endpoints.PROFILE, headers=headers)
        assert response.status_code == 200

        email = response.json()["data"].get("email")
        assert email == payload["email"]
        