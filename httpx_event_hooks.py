from httpx import Client, Request, Response
from datetime import datetime


def log_request(request: Request):
    request.extensions['start_time'] = datetime.now()
    print("REQUEST: ", request.method)

def log_response(response: Response):
    duration = datetime.now() - response.request.extensions['start_time']
    print("RESPONSE: ", response.status_code)
    print("DURATION: ", duration)

client = Client(
    base_url="http://localhost:8003",
    event_hooks={
        "response": [log_response],
        "request": [log_request],
    }
)
response = client.get('/api/v1/users/c5477af5-e71f-4824-bb34-7e5a76d666b5')

print(response)