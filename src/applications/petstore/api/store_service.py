from httpx import Response
from src.applications.petstore.models.request.store_service_requests import CreateOrderRequestModel
from src.core.clients.api_client.api_client import ApiClient


class StoreService:
    def __init__(self, api_client: ApiClient):
        self._api = api_client

    def get_inventory(self) -> Response:
        return self._api.get('/store/inventory')

    def create_order(self, order: CreateOrderRequestModel) -> Response:
        return self._api.post('/store/order', order)

    def get_order_by_id(self, id: int) -> Response:
        return self._api.get(f'/store/order/{id}')

    def delete_order_by_id(self, id: int) -> Response:
        return self._api.delete(f'/store/order/{id}')
