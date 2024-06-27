from locust import User, HttpUser, run_single_user, task
import os
import glob
import random
import logging 

from geonoderest.apiconf import GeonodeApiConf as gnConf
from geonoderest.users import GeonodeUsersHandler as gnUsers
from geonoderest.datasets import GeonodeDatasetsHandler as gnDatasets



file_path = os.path.dirname(__file__)
USER_DATA_LOCATION = os.path.join(file_path, "../datasets/users.txt")
DATASET_LOCATION =  os.path.join(file_path, "../datasets/")


def __generate_random_title__():
    return os.urandom(10).hex()

def __pick_random_user__():
  line = random.choice(list(open(USER_DATA_LOCATION, "r")))
  username, password = line.split(":")
  return (username, password)

def __pick_random_dataset__():
    gn_conf = gnConf.from_env_vars()
    geonode_datasets = gnDatasets(env=gn_conf).list( page_size=100)
    dataset = random.choice(geonode_datasets)
    return dataset
  
  
def __get_random_user_auth_header__():
    # username, password =__pick_random_user__()
    # TODO decode username password to base64 like auth_basisc in geonodectl
    # but current users are not able to login as geonode lacks setting password via API, at least in 4.2.x 
    gn_conf = gnConf.from_env_vars()
    return {"Authorization": f"Basic {gn_conf.auth_basic}"}

class GeonodeLoadTest(HttpUser):

    #wait_time = constant(1)

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
        #username, password = __pick_random_user__()
        self.client.get("/people/profile/admin")
    @task(6)
    def random_profile(self):
        username, _ = __pick_random_user__()
        self.client.get(f"/people/profile/{username}") #,auth=(username, password))
    
    @task(7)
    def random_dataset_download(self):
        dataset = __pick_random_dataset__()
        name = dataset["name"]        
        r = self.client.get(f"/datasets/geonode:{name}/dataset_download")
    
    @task(8)
    def dataset_upload(self):
        pass
      
    @task(9)
    def dataset_delete(self):
        pass

    # TODO add metadata downloads by parsing dataset object from API

if __name__ == "__main__":
    run_single_user(GeonodeLoadTest)
