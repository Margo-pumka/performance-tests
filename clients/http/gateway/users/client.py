from typing import TypedDict

from httpx import Response

from clients.http.http_client import HttpClient


class CreateUserRequestDict(TypedDict):
    """Структура данных для создания нового пользователя."""
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class UsersGatewayHttpClient(HttpClient):
    """Клиент для взаимодействия с /api/v1/users сервиса http-gateway"""

    def get_user_api(self, user_id: str) -> Response:
        """
        Получить данные пользователя по его user_id.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервиса (объект http.Response)
        """
        return self.client.get(f"/api/v1/users/{user_id}")

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Создание нового пользователя.

        :param request: Словарь с данными нового пользователя.
        :return: Ответ от сервиса (объект http.Response)
        """
        return self.client.post("/api/v1/users", json=request)
