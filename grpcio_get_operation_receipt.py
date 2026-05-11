import grpc

from contracts.services.documents.contracts.rpc_get_contract_pb2 import GetContractRequest, GetContractResponse
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import MakeTopUpOperationRequest, \
    MakeTopUpOperationResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.documents.documents_gateway_service_pb2_grpc import DocumentsGatewayServiceStub
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import OpenDebitCardAccountRequest, \
    OpenDebitCardAccountResponse
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.operations.operation_pb2 import OperationStatus
from tools.faker import fake

# Устанавливаем соединение с gRPC-сервером по адресу localhost:9003
channel = grpc.insecure_channel('localhost:9003')

# Создаём gRPC-клиент для UsersGatewayService
users_gateway_service = UsersGatewayServiceStub(channel)
# Создаём gRPC-клиент для AccountsGatewayService
accounts_gateway_service = AccountsGatewayServiceStub(channel)
# Создаём gRPC-клиент для OperationsGatewayService
operations_gateway_service = OperationsGatewayServiceStub(channel)
# Создаём gRPC-клиент для DocumentsGatewayService
documents_gateway_service = DocumentsGatewayServiceStub(channel)

# Формируем запрос на создание пользователя с рандомными данными
create_user_request = CreateUserRequest(
    email=fake.email(),
    first_name=fake.first_name(),
    last_name=fake.last_name(),
    middle_name=fake.middle_name(),
    phone_number=fake.phone_number(),
)

# Отправляем запрос и получаем ответ
create_user_response: CreateUserResponse = users_gateway_service.CreateUser(
    request=create_user_request
)
print("Create user response: ", create_user_response)

# Формируем запрос на открытие дебетового аккаунта
open_debit_card_account_request = OpenDebitCardAccountRequest(
    user_id=create_user_response.user.id
)

# Отправляем запрос и получаем ответ
open_debit_card_account_response: OpenDebitCardAccountResponse = accounts_gateway_service.OpenDebitCardAccount(
    request=open_debit_card_account_request
)
print("Open debit card account response: ", open_debit_card_account_response)

# Формируем запрос на выполнение операции пополнения счёта
make_top_up_operation_request = MakeTopUpOperationRequest(
    status=OperationStatus.OPERATION_STATUS_COMPLETED,
    amount=fake.amount(),
    account_id=open_debit_card_account_response.account.id,
    card_id=open_debit_card_account_response.account.cards[0].id
)

# Отправляем запрос и получаем ответ
make_top_up_operation_response: MakeTopUpOperationResponse = operations_gateway_service.MakeTopUpOperation(
    request=make_top_up_operation_request
)
print("Make top up operation response: ", make_top_up_operation_response)

# Формируем запрос на получение чека по операции пополнения счета
get_contract_request = GetContractRequest(
    account_id=open_debit_card_account_response.account.id
)

# Отправляем запрос и получаем ответ
get_contract_response: GetContractResponse = documents_gateway_service.GetContractDocument(
    request=get_contract_request
)
print("Get contract response: ", get_contract_response)