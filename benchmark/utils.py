import random
import os

from geonoderest.datasets import GeonodeDatasetsHandler as gnDatasets
from geonoderest.apiconf import GeonodeApiConf as gnConf

file_path = os.path.dirname(__file__)
USER_DATA_LOCATION = os.path.join(file_path, "../datasets/users.txt")
DATASET_LOCATION =  os.path.join(file_path, "../datasets/")
print(USER_DATA_LOCATION, DATASET_LOCATION)

def __get_random_user_auth_header__():
    # username, password =__pick_random_user__()
    # TODO decode username password to base64 like auth_basisc in geonodectl
    # but current users are not able to login as geonode lacks setting password via API, at least in 4.2.x 
    gn_conf = gnConf.from_env_vars()
    return {"Authorization": f"Basic {gn_conf.auth_basic}"}

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
  
def __pick_random_file__():
    import glob
    datasets = glob.glob(f"{DATASET_LOCATION}/*.geojson")
    dataset_path = random.choice(datasets)

    return dataset_path


