import httpx
import time

payload = {
  "email": f"user{time.time()}@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=payload)

create_user_response.raise_for_status()
create_user_response_data = create_user_response.json()
user_id = create_user_response_data["user"]["id"]

open_deposit_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-deposit-account",
                                           json={"userId": user_id})

open_deposit_account_response.raise_for_status()
open_deposit_account_response_data = open_deposit_account_response.json()

print(open_deposit_account_response.status_code)
print(open_deposit_account_response_data)
