from enum import StrEnum
from tools.faker import fake

from pydantic import BaseModel, Field, ConfigDict, HttpUrl


class OperationType(StrEnum):
    FEE = 'FEE'
    TOP_UP = 'TOP_UP'
    PURCHASE = 'PURCHASE'
    CASHBACK = 'CASHBACK'
    TRANSFER = 'TRANSFER'
    BILL_PAYMENT = 'BILL_PAYMENT'
    CASH_WITHDRAWAL = 'CASH_WITHDRAWAL'


class OperationStatus(StrEnum):
    FAILED = 'FAILED'
    COMPLETED = 'COMPLETED'
    IN_PROGRESS = 'IN_PROGRESS'


class GetOperationsQuerySchema(BaseModel):
    """Структура данных для получения списка операций."""
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class OperationSchema(BaseModel):
    """Структура данных операции."""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class GetOperationResponseSchema(BaseModel):
    """Структура ответа на получение информации об операции."""
    operation: OperationSchema


class OperationReceiptSchema(BaseModel):
    """Структура данных чека по операции."""
    url: HttpUrl
    document: str


class GetOperationReceiptResponseSchema(BaseModel):
    """Структура ответа на получение чека по операции."""
    receipt: OperationReceiptSchema


class GetOperationsResponseSchema(BaseModel):
    """Структура ответа на получение списка операций."""
    operations: list[OperationSchema]


class OperationsSummarySchema(BaseModel):
    """Структура данных статистики операций по счету."""
    model_config = ConfigDict(populate_by_name=True)

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class GetOperationsSummaryQuerySchema(BaseModel):
    """Структура данных для получения статистики по операциям."""
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsSummaryResponseSchema(BaseModel):
    """Структура ответа на получение статистики по операциям."""
    summary: OperationsSummarySchema


class MakeFeeOperationRequestSchema(BaseModel):
    """Структура данных для создания операции комиссии."""
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationResponseSchema(BaseModel):
    """Структура ответа на создание операции комиссии."""
    operation: OperationSchema


class MakeTopUpOperationRequestSchema(BaseModel):
    """Структура данных для создания операции пополнения."""
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeTopUpOperationResponseSchema(BaseModel):
    """Структура ответа на создание операции пополнения."""
    operation: OperationSchema


class MakeCashbackOperationRequestSchema(BaseModel):
    """Структура данных для создания операции кэшбэка."""
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeCashbackOperationResponseSchema(BaseModel):
    """Структура ответа на создание операции кэшбэка."""
    operation: OperationSchema


class MakeTransferOperationRequestSchema(BaseModel):
    """Структура данных для создания операции перевода."""
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeTransferOperationResponseSchema(BaseModel):
    """Структура ответа на создание операции перевода."""
    operation: OperationSchema


class MakePurchaseOperationRequestSchema(BaseModel):
    """Структура данных для создания операции покупки."""
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
    category: str = Field(default_factory=fake.category)


class MakePurchaseOperationResponseSchema(BaseModel):
    """Структура ответа на создание операции покупки."""
    operation: OperationSchema

class MakeBillPaymentOperationRequestSchema(BaseModel):
    """Структура данных для создания операции оплаты по счету."""
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """Структура ответа на создание операции оплаты по счету."""
    operation: OperationSchema


class MakeCashWithdrawalOperationRequestSchema(BaseModel):
    """Структура данных для создания операции снятия наличных денег."""
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """Структура ответа на создание операции снятия наличных денег."""
    operation: OperationSchema
