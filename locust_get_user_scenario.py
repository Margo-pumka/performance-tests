from http.client import responses

from locust import HttpUser, task, between

from tools.faker import fake


class GetUserScenarioUser(HttpUser):
    wait_time = between(1, 3)
    user_data: dict

    def on_start(self) -> None:
        request = {
            'email': fake.email(),
            'first_name':  fake.first_name(),
            'last_name': fake.last_name(),
            'middle_name': fake.middle_name(),
            'phone_number': fake.phone_number(),
        }
        response = self.client.post('/api/v1/users', json=request)
        self.user_data = response.json()


    @task
    def get_user(self):
        self.client.get(
            f'/api/v1/users/{self.user_data['user']['id']}',
            name='/api/v1/users/{user_id}'
        )