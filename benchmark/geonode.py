from pathlib import Path

from locust import run_single_user, task
from geonoderest.apiconf import GeonodeApiConf as gnConf

from utils import GenodeBenchmarkHttpUser


class GeonodeLoadTest(GenodeBenchmarkHttpUser):
    # wait_time = constant(1)

    # I decided to point to stable geonode when building this file because when point to
    # "https://geonode-benchmark.draven.cluster.zalf.de/" it returns 100% error

    uploaded_dataset = []

    def on_start(self):
        self.headers = self.__get_random_user_auth_header__()

    @task
    def index_page(self):
        self.client.get("/")

    # https://stackoverflow.com/questions/69338669/locust-io-and-javascript
    @task
    def dataset_landing_page(self):
        dataset = self.__pick_random_dataset__()
        pk = dataset["pk"]
        self.client.get(f"/catalogue/#/dataset/{pk}")

    @task
    def metadata_editor(self):
        dataset = self.__pick_random_dataset__()
        name = dataset["name"]
        r = self.client.get(f"/datasets/geodata:geonode:{name}/metadata")

    @task(4)
    def advanced_metadata_editor(self):
        dataset = self.__pick_random_dataset__()
        name = dataset["name"]
        self.client.get(f"/datasets/geodata:geonode:{name}/metadata_advanced")

    @task(5)
    def admin_profile(self):
        # username, password = __pick_random_user__()
        self.client.get("/people/profile/admin")

    @task(6)
    def random_profile(self):
        username, _ = self.__pick_random_user__()
        self.client.get(f"/people/profile/{username}")  # ,auth=(username, password))

    @task(7)
    def random_dataset_download(self):
        dataset = self.__pick_random_dataset__()
        name = dataset["name"]
        r = self.client.get(f"/datasets/geonode:{name}/dataset_download")

    # TODO buggy
    # @task(8)
    # def dataset_upload(self):
    #     dataset_path = Path(self.__pick_random_file__())

    #     files = [
    #         (
    #             "base_file",
    #             (
    #                 dataset_path.name,
    #                 open(str(dataset_path), "rb"),
    #                 "application/geo+json",
    #             ),
    #         ),
    #     ]

    #     params = {
    #         # layer permissions
    #         "permissions": '{ "users": {"AnonymousUser": ["view_resourcebase"]} , "groups":{}}',
    #         "mosaic": False,
    #         "time": str(False),
    #         "charset": "UTF-8",
    #         "non_interactive": True,
    #     }
    #     r = self.client.post(
    #         "/api/v2/uploads/upload", files=files, headers=self.headers, params=params
    #     )

    #     gn_conf = gnConf.from_env_vars()
    #     exec_id = r.json()["upload"]["execution_id"]
    #     pk = self.__wait_and_get_upload_pk__(exec_id, gnConf)
    #     self.uploaded_dataset.append(pk)

    @task(9)
    def dataset_delete(self):
        pass


if __name__ == "__main__":
    run_single_user(GeonodeLoadTest)
