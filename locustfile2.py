from locust import HttpLocust, TaskSet, task


class GeonodeLoadTest(TaskSet):
    host = "https://geonode-benchmark.draven.cluster.zalf.de/"

    # when locust file start executing on_start() will be called first
    def on_start(self):
        self.client.get("/")

    @seq_task(1)  # After on_start(), login() will be called
    @task(2)  # 2 times login() will be called
    def login(self):
        self.client.post(
            "/account/login/", {"username": "admin", "password": "geonode"}
        )

    @seq_task(2)  # After login(), get_dashboard will be called
    @task(4)  # 4 times get_dashboard() will be called
    def get_dashboard(self):
        self.client.get("/account/dashboard")

    @seq_task(3)  # After get_dashboard(), logout() will be called 1 time( by Default)
    def logout(self):
        self.client.post("/account/logout")


class MyWebsiteUser(HttpLocust):
    task_set = GeonodeLoadTest
    min_wait = 100  # miliseconds
    max_wait = 5000  # miliseconds
    # same as wait_time = between(0.100, 5)
