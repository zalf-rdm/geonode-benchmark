import random
import os
import glob

from locust import HttpUser

from geonoderest.apiconf import GeonodeApiConf as gnConf


class GenodeBenchmarkHttpUser(HttpUser):
    abstract = True
    all_datasets = None

    FILE_PATH = os.path.dirname(__file__)
    USER_DATA_LOCATION = os.path.join(FILE_PATH, "../datasets/users.txt")
    DATASET_LOCATION = os.path.join(FILE_PATH, "../datasets/")

    def __get_random_user_auth_header__(self):
        # username, password =__pick_random_user__()
        # TODO decode username password to base64 like auth_basisc in geonodectl
        # but current users are not able to login as geonode lacks setting password via API, at least in 4.2.x
        gn_conf = gnConf.from_env_vars()
        return {"Authorization": f"Basic {gn_conf.auth_basic}"}

    def on_start(self):
        """
        Called when the user starts running.

        This is the place to perform any setup that should happen before the user
        starts running, such as setting up the headers with a random user.

        """
        self.headers = self.__get_random_user_auth_header__()

    # TODO write a method that deletes all uploads
    def on_stop(self):
        pass

    def __generate_random_title__(self):
        return os.urandom(10).hex()

    def __pick_random_user__(self):
        line = random.choice(list(open(self.USER_DATA_LOCATION, "r")))
        username, password = line.split(":")
        return (username, password)

    def __pick_random_dataset__(self):
        if self.all_datasets is None:
            self.all_datasets = self.client.get("/api/v2/datasets/?page_size=100", headers=self.headers).json()["datasets"]
        dataset = random.choice(self.all_datasets)
        return dataset

    def __pick_random_file__(self):
        datasets = glob.glob(f"{self.DATASET_LOCATION}/*.geojson")
        dataset_path = random.choice(datasets)

        return dataset_path

