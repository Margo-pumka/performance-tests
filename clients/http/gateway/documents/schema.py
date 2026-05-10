from pydantic import BaseModel, HttpUrl


class DocumentSchema(BaseModel):
    """Структура данных документа."""
    document: str
    url: HttpUrl


class GetTariffDocumentResponseSchema(BaseModel):
    """Структура данных для получения тарифа по счету."""
    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """Структура данных для получения контракта по счету."""
    contract: DocumentSchema