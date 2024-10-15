
import time
from pathlib import Path

from locust import run_single_user, task, between

from utils import GenodeBenchmarkHttpUser


class GeonodeLoadTest(GenodeBenchmarkHttpUser):
    wait_time = between(1, 3)
    
    uploaded_dataset = []

    def on_start(self):
        self.headers = self.__get_random_user_auth_header__()

    @task(1)
    def get_favicon(self):
        self.client.get("/static/geonode/img/favicon.ico")

    @task(6)
    def get_index_page(self):
        self.client.get("/")

    # https://stackoverflow.com/questions/69338669/locust-io-and-javascript
    @task(6)
    def get_dataset_landing_page(self):
        dataset = self.__pick_random_dataset__()
        pk = dataset["pk"]
        self.client.get(f"/catalogue/#/dataset/{pk}")

    @task(4)
    def get_metadata_editor(self):
        dataset = self.__pick_random_dataset__()
        name = dataset["name"]
        r = self.client.get(f"/datasets/geodata:geonode:{name}/metadata")

    @task(2)
    def get_advanced_metadata_editor(self):
        dataset = self.__pick_random_dataset__()
        name = dataset["name"]
        self.client.get(f"/datasets/geodata:geonode:{name}/metadata_advanced")

    @task(2)
    def get_admin_profile(self):
        # username, password = __pick_random_user__()
        self.client.get("/people/profile/admin")

    @task(6)
    def get_random_profile(self):
        username, _ = self.__pick_random_user__()
        self.client.get(f"/people/profile/{username}")  # ,auth=(username, password))

    @task(4)
    def get_random_dataset_download(self):
        dataset = self.__pick_random_dataset__()
        name = dataset["name"]
        r = self.client.get(f"/datasets/geonode:{name}/dataset_download")

    @task(2)
    def get_random_dataset_wms_legend_png(self):
        dataset = self.__pick_random_dataset__()
        links = dataset["links"]
        url = None
        for link in links:
          if link["extension"] == "png" and link["name"] == "Legend":
            url = link["url"]
            break
        
        if url is not None:
          self.client.get(url)

    @task(2)
    def get_random_dataset_wms_png(self):
        dataset = self.__pick_random_dataset__()
        links = dataset["links"]
        url = None
        for link in links:
          if link["extension"] == "png" and link["name"] == "PNG":
            url = link["url"]
            break
        
        if url is not None:
          self.client.get(url)


    @task(2)
    def get_random_dataset_wms_xml(self):
        dataset = self.__pick_random_dataset__()
        links = dataset["links"]
        url = None
        for link in links:
          if link["extension"] == "xml":
            url = link["url"]
            break
        
        if url is not None:
          self.client.get(url)

    @task(2)
    def get_random_dataset_wms_jpg(self):
        dataset = self.__pick_random_dataset__()
        links = dataset["links"]
        url = None
        for link in links:
          if link["extension"] == "jpg":
            url = link["url"]
            break
        
        if url is not None:
          self.client.get(url)
          

    @task(2)
    def get_random_dataset_wms_pdf(self):
        dataset = self.__pick_random_dataset__()
        links = dataset["links"]
        url = None
        for link in links:
          if link["extension"] == "pdf":
            url = link["url"]
            break
        
        if url is not None:
          self.client.get(url)

    @task(2)
    def upload_dataset(self):
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
    def delete_dataset(self):
      
      if len(self.uploaded_dataset) > 0:
        i = str(self.uploaded_dataset.pop())
        self.client.delete(f"api/v2/resources/{i}/delete")


if __name__ == "__main__":
    run_single_user(GeonodeLoadTest)
