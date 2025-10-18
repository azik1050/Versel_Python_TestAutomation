from src.application.models.response.user_service_responses import GetUserResponseModel
from src.application.utils.api_assertions import ApiAssertions


def test_get_valid_user(user_api):
    response = user_api.get_user_by_username("Azimjon")
    ApiAssertions.assert_status_code(response, 200)

    user = GetUserResponseModel(**response.json())
