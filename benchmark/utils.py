import random
import os
import glob
import logging
import sys
import time
import re

from locust import HttpUser
from locust.exception import RescheduleTask

from geonoderest.datasets import GeonodeDatasetsHandler as gnDatasets
from geonoderest.apiconf import GeonodeApiConf as gnConf
from geonoderest.executionrequest import (
    GeonodeExecutionRequestHandler as gnExecutionRequest,
)


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
        gn_conf = gnConf.from_env_vars()
        if self.all_datasets is None:
            self.all_datasets = gnDatasets(env=gn_conf).list(page_size=100)
        dataset = random.choice(self.all_datasets)
        return dataset

    def __pick_random_file__(self):
        datasets = glob.glob(f"{self.DATASET_LOCATION}/*.geojson")
        dataset_path = random.choice(datasets)

        return dataset_path

    def __wait_and_get_upload_pk__(self, execid: str, gnConf: gnConf) -> int:
        """
        Wait for the upload to finish and retrieve the primary key (pk) of the upload.

        Args:
            execid (str): The ID of the execution.

        Returns:
            int: The primary key (pk) of the upload.

        Raises:
            SystemExit: If the upload fails or the pk ID cannot be found.
        """
        gn_execreq = gnExecutionRequest(gnConf)
        r_exec = gn_execreq.get(exec_id=execid, page_size=100)
        t = 0
        while r_exec["status"] != "finished" and r_exec["status"] != "failed":
            r_exec = gn_execreq.get(exec_id=execid, page_size=100)
            t += 5

        if r_exec["status"] == "failed":
            raise RescheduleTask("Could not find pk id of upload ...")

        detail_url = r_exec["output_params"]["resources"][0]["detail_url"]
        match = re.search(r"/(\d+)$", detail_url)
        if match:
            return int(match.group(1))
        else:
            raise RescheduleTask("Could not find pk id of upload ...")
