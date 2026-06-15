from locust import HttpUser, between, task

from tools.faker import fake


class OpenDebitCardAccountScenarioUser(HttpUser):
    wait_time = between(1, 3)
    user_data: dict

    def on_start(self) -> None:
        request = {
            'email': fake.email(),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'middle_name': fake.middle_name(),
            'phone_number': fake.phone_number(),
        }
        response = self.client.post('/api/v1/users', json=request)

        self.user_data = response.json()

    @task
    def open_debit_card_account(self):
        self.client.post('/api/v1/accounts/open-debit-card-account', json={'userId': self.user_data['user']['id']})