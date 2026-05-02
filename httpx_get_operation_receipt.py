import httpx
import time

create_user_payload = {
  "email": f"user{time.time()}@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)

create_user_response.raise_for_status()
create_user_response_data = create_user_response.json()
user_id = create_user_response_data["user"]["id"]

open_credit_card_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account",
                                           json={"userId": user_id})

open_credit_card_account_response.raise_for_status()
open_credit_card_account_response_data = open_credit_card_account_response.json()

account_id = open_credit_card_account_response_data["account"]["id"]
card_id = open_credit_card_account_response_data["account"]["cards"][0]["id"]

make_purchase_operation_payload = {
  "status": "IN_PROGRESS",
  "amount": 77.99,
  "cardId": card_id,
  "accountId": account_id,
  "category": "taxi"
}

make_purchase_operation_response = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation",
                                              json=make_purchase_operation_payload)

make_purchase_operation_response.raise_for_status()
make_purchase_operation_response_data = make_purchase_operation_response.json()
operation_id = make_purchase_operation_response_data["operation"]["id"]



get_receipt_response = httpx.get(f"http://localhost:8003/api/v1/operations/operation-receipt/{operation_id}")

get_receipt_response.raise_for_status()
get_receipt_response_data = get_receipt_response.json()

print(get_receipt_response_data)