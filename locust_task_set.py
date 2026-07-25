from locust import HttpUser, TaskSet, between, task


class MySequentialTaskSet(TaskSet):
    wait_time = between(1, 3)

    @task
    def task_one(self):
        self.client.get("/page1")

    @task
    def task_two(self):
        self.client.get("/page2")

    @task
    def task_three(self):
        self.client.get("/page3")


class MyTaskSet(TaskSet):
    wait_time = between(1, 3)

    @task
    def task_one(self):
        self.client.get("/page1")

    @task
    def task_two(self):
        self.client.get("/page2")

class MyUser(HttpUser):
    wait_time = between(1, 3)
    tasks = [MyTaskSet]
