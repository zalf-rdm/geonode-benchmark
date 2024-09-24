
import time
from pathlib import Path

from locust import run_single_user, task, between

from utils import GenodeBenchmarkHttpUser


class GeonodeDevLoadTest(GenodeBenchmarkHttpUser):
    wait_time = between(1,5)

    uploaded_dataset = []
    def on_start(self):
        self.headers = self.__get_random_user_auth_header__()
    # TODO buggy
 
    @task(1)
    def dataset_upload(self):
        dataset_path = Path(self.__pick_random_file__())

        files = [
            (
                "base_file",
                (
                    dataset_path.name,
                    open(str(dataset_path), "rb"),
                    "application/geo+json",
                ),
            ),
        ]

        params = {
            # layer permissions
            "permissions": '{ "users": {"AnonymousUser": ["view_resourcebase"]} , "groups":{}}',
            "mosaic": False,
            "time": str(False),
            "charset": "UTF-8",
            "non_interactive": True,
        }
        r = self.client.post(
            "/api/v2/uploads/upload", files=files, headers=self.headers, params=params
        )

        exec_id = r.json()["execution_id"]
        
        status = "pending"
        i = 0
        while status != "finished" or i==100:
            r_exec = self.client.get(f"/api/v2/executionrequest/{exec_id}", headers=self.headers).json()
            status = r_exec['request']['status']
            time.sleep(1)
            i += 1

        pk = r_exec["request"]["output_params"]["resources"][0]["id"]
        self.uploaded_dataset.append(pk)

    @task(1)
    def dataset_delete(self):
      
      if len(self.uploaded_dataset) > 0:
        self.client.delete(f"/resources/{self.uploaded_dataset.pop()}/delete")


if __name__ == "__main__":
    run_single_user(GeonodeDevLoadTest)
