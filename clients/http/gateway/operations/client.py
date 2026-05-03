from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.http_client import HttpClient


class GetOperationsQueryDict(TypedDict):
    """Структура данных для получения списка операций."""
    accountId: str

class GetOperationsSummaryQueryDict(TypedDict):
    """Структура данных для получения статистики по операциям."""
    accountId: str

class MakeFeeOperationRequestDict(TypedDict):
    """Структура данных для создания операции комиссии."""
    status: str
    amount: int
    cardId: str
    accountId: str

class MakeTopUpOperationRequestDict(TypedDict):
    """Структура данных для создания операции пополнения."""
    status: str
    amount: int
    cardId: str
    accountId: str

class MakeCashbackOperationRequestDict(TypedDict):
    """Структура данных для создания операции кэшбэка."""
    status: str
    amount: int
    cardId: str
    accountId: str

class MakeTransferOperationRequestDict(TypedDict):
    """Структура данных для создания операции перевода."""
    status: str
    amount: int
    cardId: str
    accountId: str

class MakePurchaseOperationRequestDict(TypedDict):
    """Структура данных для создания операции покупки."""
    status: str
    amount: int
    cardId: str
    accountId: str
    category: str

class MakeBillPaymentOperationRequestDict(TypedDict):
    """Структура данных для создания операции оплаты по счету."""
    status: str
    amount: int
    cardId: str
    accountId: str

class MakeCashWithdrawalPaymentOperationRequestDict(TypedDict):
    """Структура данных для создания операции снятия наличных денег."""
    status: str
    amount: int
    cardId: str
    accountId: str

class OperationsGatewayHTTPClient(HttpClient):
    """Клиент для взаимодействия с /api/v1/operations сервиса http-gateway"""

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Выполняет запрос на получение списка операций для определенного счета.

        :param query: Словарь с accountId.
        :return: Ответ от сервиса (объект http.Response)
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет запрос на получение чека по операции.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервиса (объект http.Response)
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Выполняет запрос на получение информации об операции.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервиса (объект http.Response)
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Выполняет запрос на получение статистики по операциям для определенного счета.

        :param query: Словарь с accountId.
        :return: Ответ от сервиса (объект http.Response)
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет запрос на создание операции комиссии.

        :param request: Словарь с данными об операции.
        :return: Ответ от сервиса (объект http.Response)
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет запрос на создание операции пополнения.

        :param request: Словарь с данными об операции.
        :return: Ответ от сервиса (объект http.Response)
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Выполняет запрос на создание операции кэшбэка.

        :param request: Словарь с данными об операции.
        :return: Ответ от сервиса (объект http.Response)
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Выполняет запрос на создание операции перевода.

        :param request: Словарь с данными об операции.
        :return: Ответ от сервиса (объект http.Response)
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет запрос на создание операции покупки.

        :param request: Словарь с данными об операции.
        :return: Ответ от сервиса (объект http.Response)
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Выполняет запрос на создание операции оплаты по счету.

        :param request: Словарь с данными об операции.
        :return: Ответ от сервиса (объект http.Response)
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalPaymentOperationRequestDict) -> Response:
        """
        Выполняет запрос на создание операции снятия наличных денег.

        :param request: Словарь с данными об операции.
        :return: Ответ от сервиса (объект http.Response)
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)