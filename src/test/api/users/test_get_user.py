from src.application.entities.user_factory import UserFactory
from src.application.models.response.user_service_responses import GetUserResponseModel
from src.application.utils.api_assertions import ApiAssertions


def test_get_valid_user(user_api):
    # create a user
    created_user = UserFactory.create_random_user()
    user_api.create_user(created_user)

    # test part
    response = user_api.get_user_by_username(created_user.username)

    # Validate status code
    ApiAssertions.assert_status_code(response, 200)
    # Validate response model
    ApiAssertions.validate_response_model(response, GetUserResponseModel)
