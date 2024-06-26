from locust import task, run_single_user
from locust import FastHttpUser


class GeonodeLoadTest(FastHttpUser):
    host = "https://stable.demo.geonode.org"
    login = "forrbodo@gmail.com"
    password = "geonode"

    @task
    def login(self):
        with self.client.request(
            "GET",
            "/account/login/",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/account/login/",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": "csrftoken=9DG3EElOKVCQIQGntbZVBWs4Rz4pX4Nn; sessionid=dxt71aef1wa2za5352u4qofxxh2fsg54; _ga=GA1.2.701197513.1719407312; _gid=GA1.2.2122075933.1719407312; _gat=1; _ga_G41DE0P9ZT=GS1.2.1719407311.5.0.1719407311.0.0.0",
            },
            data=f"csrfmiddlewaretoken=KjvO2pGAXD8Hzbv6eyNqQwRFPbxgNoziJM1HwTRexoAn7R1jxzCbhi9zwArvAicv&login={self.login}&password={self.password}&next=%2F",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/",
            headers={},
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(GeonodeLoadTest)
