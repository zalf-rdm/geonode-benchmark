from pathlib import Path

from locust import HttpUser, run_single_user, task

from utils import (
    __pick_random_file__,
    __generate_random_title__,
    __pick_random_user__,
    __pick_random_dataset__,
    __get_random_user_auth_header__,
)


class GeonodeLoadTest(HttpUser):

    # wait_time = constant(1)

    # I decided to point to stable geonode when building this file because when point to
    # "https://geonode-benchmark.draven.cluster.zalf.de/" it returns 100% error

    uploaded_dataset = None

    def on_start(self):
        self.headers = __get_random_user_auth_header__()

    @task
    def index_page(self):
        self.client.get("/")

    # https://stackoverflow.com/questions/69338669/locust-io-and-javascript
    @task
    def dataset_landing_page(self):

        dataset = __pick_random_dataset__()
        pk = dataset["pk"]
        self.client.get(f"/catalogue/#/dataset/{pk}")

    @task
    def metadata_editor(self):
        dataset = __pick_random_dataset__()
        name = dataset["name"]
        r = self.client.get(f"/datasets/geodata:geonode:{name}/metadata")

    @task(4)
    def advanced_metadata_editor(self):
        dataset = __pick_random_dataset__()
        name = dataset["name"]
        self.client.get(f"/datasets/geodata:geonode:{name}/metadata_advanced")

    @task(5)
    def admin_profile(self):
        # username, password = __pick_random_user__()
        self.client.get("/people/profile/admin")

    @task(6)
    def random_profile(self):
        username, _ = __pick_random_user__()
        self.client.get(f"/people/profile/{username}")  # ,auth=(username, password))

    @task(7)
    def random_dataset_download(self):
        dataset = __pick_random_dataset__()
        name = dataset["name"]
        r = self.client.get(f"/datasets/geonode:{name}/dataset_download")

    @task(8)
    def dataset_upload(self):
        dataset_path = Path(__pick_random_file__())
        
        files = [
            ("base_file", (dataset_path.name, open(str(dataset_path), "rb"),"application/geo+json" )),
        ]

        params = {
            # layer permissions
            "permissions": '{ "users": {"AnonymousUser": ["view_resourcebase"]} , "groups":{}}',
            "mosaic": False,
            "time": str(False),
            "charset": "UTF-8",
            "non_interactive": True,
        }
        self.client.post("/api/v2/uploads/upload", files=files, headers=self.headers, params=params)

    @task(9)
    def dataset_delete(self):
        pass

    # TODO add metadata downloads by parsing dataset object from API


if __name__ == "__main__":
    run_single_user(GeonodeLoadTest)
