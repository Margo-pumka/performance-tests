from pydantic import BaseModel, EmailStr, UUID4


class CreateUserRequestSchema(BaseModel):
    """
    Структура данных для создания нового пользователя.
    """
    email: EmailStr
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str

class UserSchema(CreateUserRequestSchema):
    """
    Описание структуры пользователя.
    """
    id: UUID4

class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа получения пользователя.
    """
    user: UserSchema
