from locust import task, run_single_user, between
from locust import FastHttpUser, HttpUser
import os
import glob


class GeonodeLoadTest(HttpUser):
    between(1, 5)

    # I decided to point to stable geonode when building this file because when point to
    # "https://geonode-benchmark.draven.cluster.zalf.de/" it returns 100% error
    host = "https://geonode-benchmark.draven.cluster.zalf.de"
    login = os.environ["GEONODE_LOGIN"]
    password = os.environ["GEONODE_PASSWORD"]
    csrfmiddlewaretoken = os.environ["GEONODE_CSRFMIDDLEWARETOKEN"]

    dataset_list = glob.glob("./datasets/*.geojson")
    open_dataset_nr = 1825
    dataset_title_download = "Dia_phan_Tinh"
    dataset_title_upload = "test_upload"
    type_file = "application/json"
    file = "./datasets/1.geojson"
    datasets = [
        (
            "geojson_file",
            (
                "test_upload",
                open("./datasets/0.geojson", "rb"),
                "application/json",
            ),
        ),
    ]
    dataset_title = "dataset_title"
    dataset_nr_to_upload_metadata = 1
    metada_title = "metada_example.xml"
    metada_file = "./datasets/metada_example.xml"
    metadata = (metada_title, open(metada_file, "rb"), "text/xml")

    dataset_nr_to_delete = 1

    @task
    def t(self):
        with self.client.get(
            "/",
            catch_response=True,
        ) as resp:
            pass
        with self.client.get(
            "/account/login/",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/account/login/",
            data=f"csrfmiddlewaretoken={self.csrfmiddlewaretoken}&login={self.login}&password={self.geonode}&remember=on&next=%2F",
            catch_response=True,
        ) as resp:
            pass
        with self.client.get(  # 2.Choose and open a dataset
            f"/catalogue/#/dataset/{self.open_dataset_nr}",
            catch_response=True,
        ) as resp:
            pass
        with self.client.get(  # 3.Check the metadata
            f"/datasets/geonode_master_data:geonode:{self.dataset_title_download}/metadata_detail",
            catch_response=True,
        ) as resp:
            pass
        with self.client.get(  # 4.Dataset Download
            f"/datasets/geonode:{self.dataset_title_download}/dataset_download",
            catch_response=True,
        ) as resp:
            pass
        with self.client.get(  # 5.UPLOAD DATASET: Go to upload dataset page
            "/upload/dataset",
            catch_response=True,
        ) as resp:
            pass
        # Sometimes can't work in the stablegeonode because of flood
        with self.client.post(  # 5.UPLOAD DATASET: Upload dataset with API
            "/api/v2/uploads/upload",
            headers={
                "Authorization": "Basic dXNlcjpwYXNzd29yZA==",
            },
            files=[
                (
                    "geojson_file",
                    (
                        "test_upload2",
                        open("./datasets/0.geojson", "rb"),
                        "application/json",
                    ),
                )
            ],
            catch_response=True,
        ) as resp:
            pass
        # with self.client.put(  # TODO Upload Metada with API
        #     f"/api/v2/datasets/{self.dataset_nr_to_upload_metadata}/metadata",
        #     headers={"Authorization": "Basic dXNlcjpwYXNzd29yZA=="},
        #     files=[self.metadata],
        #     catch_response=True,
        # ) as resp:
        #     pass
        # with self.client.delete(  # TODO Delete dataset
        #     f"/api/v2/resources/{self.dataset_nr_to_delete}/delete",
        #     headers={"Authorization": "Basic dXNlcjpwYXNzd29yZA=="},
        #     catch_response=True,
        # ) as resp:
        #     pass
        with self.client.post(  # logout
            "/account/logout/",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
            },
            data="csrfmiddlewaretoken=gzjZOaSZnMNJZVD3rjvrWvGRbAeMIMzDJhC0oAs7H8xXqV76WxWShWTPHzm7CQfQ",
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(GeonodeLoadTest)
