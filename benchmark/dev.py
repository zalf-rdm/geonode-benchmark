from pathlib import Path

from locust import run_single_user, task
from geonoderest.apiconf import GeonodeApiConf as gnConf

from utils import GenodeBenchmarkHttpUser


class GeonodeLoadTest(GenodeBenchmarkHttpUser):
    # wait_time = constant(1)

    uploaded_dataset = []
    def on_start(self):
        self.headers = self.__get_random_user_auth_header__()
    # TODO buggy
    @task(8)
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

        gn_conf = gnConf.from_env_vars()

        exec_id = r.json()["execution_id"]
        
        status = "pending"
        i = 0
        while status != "finished" or i==100:
            r_exec = self.client.get(f"/api/v2/executionrequest/{exec_id}", headers=self.headers).json()
            print(r_exec)
            status = r_exec['status']
            print(status, i)
            i += 1
        pk = r_exec["output_params"]["resources"]["id"]
        self.uploaded_dataset.append(pk)

    @task(9)
    def dataset_delete(self):
        pass


if __name__ == "__main__":
    run_single_user(GeonodeLoadTest)