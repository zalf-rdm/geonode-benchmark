from locust import task, run_single_user, between
from locust import FastHttpUser, HttpUser
import os
import glob


class GeonodeLoadTest(HttpUser):
    between(1, 5)

    @task
    def t(self):
        with self.client.post(  # 5.UPLOAD DATASET: Upload dataset with API
            "/api/v2/uploads/upload",
            headers={"Authorization": "Basic dXNlcjpwYXNzd29yZA=="},
            files=[
                (
                    "geojson_file",
                    (
                        "0.geojson",
                        open("./datasets/0.geojson", "rb"),
                        "application/json",
                    ),
                )
            ],
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(GeonodeLoadTest)
