from src.application.entities.user_factory import UserFactory
from src.application.models.response.user_service_responses import CreateUserResponse
from src.application.utils.api_assertions import ApiAssertions


def test_create_user_success(user_api):
    response = user_api.create_user(user=UserFactory.create_random_user())
    body = response.json()

    # Validate status code
    ApiAssertions.assert_status_code(response, 200)

    # Validate response body
    ApiAssertions.validate_response_model(response, CreateUserResponse)
    assert body["code"] == 200, "Invalid response body code"
    assert body["type"] == "unknown", "Invalid response body type"


