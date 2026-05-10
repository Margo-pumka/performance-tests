from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.gateway.client import build_gateway_http_client
from clients.http.http_client import HttpClient


class GetOperationsQueryDict(TypedDict):
    """Структура данных для получения списка операций."""
    accountId: str

class OperationDict(TypedDict):
    """Структура данных операции."""
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str

class GetOperationResponseDict(TypedDict):
    """Структура ответа на получение информации об операции."""
    operation: OperationDict

class OperationReceiptDict(TypedDict):
    """Структура данных чека по операции."""
    url: str
    document: str

class GetOperationReceiptResponseDict(TypedDict):
    """Структура ответа на получение чека по операции."""
    receipt: OperationReceiptDict

class GetOperationsResponseDict(TypedDict):
    """Структура ответа на получение списка операций."""
    operations: list[OperationDict]

class OperationsSummaryDict(TypedDict):
    """Структура данных статистики операций по счету."""
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float

class GetOperationsSummaryQueryDict(TypedDict):
    """Структура данных для получения статистики по операциям."""
    accountId: str

class GetOperationsSummaryResponseDict(TypedDict):
    """Структура ответа на получение статистики по операциям."""
    summary: OperationsSummaryDict

class MakeFeeOperationRequestDict(TypedDict):
    """Структура данных для создания операции комиссии."""
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeFeeOperationResponseDict(TypedDict):
    """Структура ответа на создание операции комиссии."""
    operation: OperationDict

class MakeTopUpOperationRequestDict(TypedDict):
    """Структура данных для создания операции пополнения."""
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeTopUpOperationResponseDict(TypedDict):
    """Структура ответа на создание операции пополнения."""
    operation: OperationDict

class MakeCashbackOperationRequestDict(TypedDict):
    """Структура данных для создания операции кэшбэка."""
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeCashbackOperationResponseDict(TypedDict):
    """Структура ответа на создание операции кэшбэка."""
    operation: OperationDict

class MakeTransferOperationRequestDict(TypedDict):
    """Структура данных для создания операции перевода."""
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeTransferOperationResponseDict(TypedDict):
    """Структура ответа на создание операции перевода."""
    operation: OperationDict

class MakePurchaseOperationRequestDict(TypedDict):
    """Структура данных для создания операции покупки."""
    status: str
    amount: float
    cardId: str
    accountId: str
    category: str

class MakePurchaseOperationResponseDict(TypedDict):
    """Структура ответа на создание операции покупки."""
    operation: OperationDict

class MakeBillPaymentOperationRequestDict(TypedDict):
    """Структура данных для создания операции оплаты по счету."""
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeBillPaymentOperationResponseDict(TypedDict):
    """Структура ответа на создание операции оплаты по счету."""
    operation: OperationDict

class MakeCashWithdrawalOperationRequestDict(TypedDict):
    """Структура данных для создания операции снятия наличных денег."""
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """Структура ответа на создание операции снятия наличных денег."""
    operation: OperationDict

class OperationsGatewayHTTPClient(HttpClient):
    """Клиент для взаимодействия с /api/v1/operations сервиса http-gateway"""

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Выполняет запрос на получение списка операций для определенного счета.

        :param query: Словарь с accountId.
        :return: Ответ от сервиса (объект httpx.Response)
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет запрос на получение чека по операции.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервиса (объект httpx.Response)
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Выполняет запрос на получение информации об операции.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервиса (объект httpx.Response)
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Выполняет запрос на получение статистики по операциям для определенного счета.

        :param query: Словарь с accountId.
        :return: Ответ от сервиса (объект httpx.Response)
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет запрос на создание операции комиссии.

        :param request: Словарь с данными об операции.
        :return: Ответ от сервиса (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет запрос на создание операции пополнения.

        :param request: Словарь с данными об операции.
        :return: Ответ от сервиса (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Выполняет запрос на создание операции кэшбэка.

        :param request: Словарь с данными об операции.
        :return: Ответ от сервиса (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Выполняет запрос на создание операции перевода.

        :param request: Словарь с данными об операции.
        :return: Ответ от сервиса (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет запрос на создание операции покупки.

        :param request: Словарь с данными об операции.
        :return: Ответ от сервиса (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Выполняет запрос на создание операции оплаты по счету.

        :param request: Словарь с данными об операции.
        :return: Ответ от сервиса (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Выполняет запрос на создание операции снятия наличных денег.

        :param request: Словарь с данными об операции.
        :return: Ответ от сервиса (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operations(self, account_id: str)-> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query=query)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        response = self.get_operation_receipt_api(operation_id=operation_id)
        return response.json()

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id=operation_id)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query=query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
            category="hobby"
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()

def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())