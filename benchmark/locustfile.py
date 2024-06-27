from locust import task, run_single_user
from locust import FastHttpUser
import os


class GeonodeLoadTest(FastHttpUser):
    # I decided to point to stable geonode when building this file because when point to
    # "https://geonode-benchmark.draven.cluster.zalf.de/" it returns 100% error
    host = "https://stable.demo.geonode.org"
    login = os.environ["GEONODE_LOGIN"]
    password = os.environ["GEONODE_PASSWORD"]
    open_dataset_nr = 1825
    dataset_title = "Dia_phan_Tinh"
    type_file = "application/json"
    file = "./benchmark/datasets.1.geojson"
    datasets = (
        "geojson_file",
        (
            "test.geojson",
            open("./datasets/0.geojson", "rb"),
            "application/json",
        ),
    )

    @task
    def login(self):
        with self.client.get(
            "/",
            catch_response=True,
        ) as resp:
            pass
        with self.client.post(  # 1.Login
            "/account/login/",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": "csrftoken=9DG3EElOKVCQIQGntbZVBWs4Rz4pX4Nn; sessionid=dxt71aef1wa2za5352u4qofxxh2fsg54; _ga=GA1.2.701197513.1719407312; _gid=GA1.2.2122075933.1719407312; _gat=1; _ga_G41DE0P9ZT=GS1.2.1719407311.5.0.1719407311.0.0.0",
            },
            data=f"csrfmiddlewaretoken=KjvO2pGAXD8Hzbv6eyNqQwRFPbxgNoziJM1HwTRexoAn7R1jxzCbhi9zwArvAicv&login={self.login}&password={self.password}&next=%2F",
            catch_response=True,
        ) as resp:
            pass
        with self.client.get(  # 2.Choose and open a dataset
            f"/catalogue/#/dataset/{self.open_dataset_nr}",
            catch_response=True,
        ) as resp:
            pass
        with self.client.get(  # 3.Check the metadata
            f"/datasets/geonode_master_data:geonode:{self.dataset_title}/metadata_detail",
            catch_response=True,
        ) as resp:
            pass
        with self.client.get(  # 4.Dataset Download
            f"/datasets/geonode:{self.dataset_title}/dataset_download",
            catch_response=True,
        ) as resp:
            pass
        with self.client.get(  # 5.UPLOAD DATASET: Go to upload dataset page
            "https://stable.demo.geonode.org/catalogue/#/upload/dataset",
            catch_response=True,
        ) as resp:
            pass
        with self.client.post(  # 5.UPLOAD DATASET: Upload dataset with API
            "/api/v2/uploads/upload",
            headers={
                "Authorization": "Basic dXNlcjpwYXNzd29yZA==",
            },
            files=[self.datasets],
            catch_response=True,
        ) as resp:
            pass
        with self.client.get(  # TODO Edit Advance metadata
            "/",
            catch_response=True,
        ) as resp:
            pass
        with self.client.delete(  # TODO Delete dataset
            "/api/v2/resources/1",
            headers={"Authorization": "Basic dXNlcjpwYXNzd29yZA=="},
            catch_response=True,
        ) as resp:
            pass
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
