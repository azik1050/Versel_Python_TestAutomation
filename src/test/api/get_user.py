from src.application.models.response.user_service_models import GetUserRequestModel


def test_get_user(user_api):
    response = user_api.get_user_by_username("Azimjon")
    assert response.status_code == 200, "Response code is invalid"

    user = GetUserRequestModel(**response.json())
