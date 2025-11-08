from httpx import Response
from src.application.models.request.store_service_requests import CreateOrderRequestModel
from src.core.clients.api_client import ApiClient


class StoreService(ApiClient):
    def __init__(self, base_url: str):
        super().__init__(base_url)

    def get_inventory(self) -> Response:
        return self._get('/store/inventory')

    def create_order(self, order: CreateOrderRequestModel) -> Response:
        return self._post('/store/order', order.model_dump())

    def get_order_by_id(self, id: int) -> Response:
        return self._get(f'/store/order/{id}')

    def delete_order_by_id(self, id: int) -> Response:
        return self._delete(f'/store/order/{id}')
