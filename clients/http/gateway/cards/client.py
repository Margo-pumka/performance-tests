from typing import TypedDict

from httpx import Response

from clients.http.http_client import HttpClient


class IssueCardRequestDict(TypedDict):
    """Структура данных для создания новой карты (виртуальной или физической)."""
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HttpClient):
    """Клиент для взаимодействия с /api/v1/cards сервиса http-gateway"""

    def issue_virtual_card_api(self, request: IssueCardRequestDict) -> Response:
        """
        Создание виртуальной карты.

        :param request: Словарь с идентификаторами пользователя.
        :return: Ответ от сервиса (объект http.Response)
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssueCardRequestDict) -> Response:
        """
        Создание физической карты.

        :param request: Словарь с идентификаторами пользователя.
        :return: Ответ от сервиса (объект http.Response)
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)
