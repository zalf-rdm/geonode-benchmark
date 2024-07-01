import random
import string
import logging
import argparse
import os
import glob
import time
from pathlib import Path
import sys

from geonoderest.apiconf import GeonodeApiConf as gnConf
from geonoderest.users import GeonodeUsersHandler as gnUsers
from geonoderest.datasets import GeonodeDatasetsHandler as gnDatasets

import geopandas as gpd
import geodatasets as gds

# script collection to prepare several steps to run the benchmark


USER_DATA_LOCATION = "datasets/users.txt"
DATASET_LOCATION = "datasets/"


def configure_logging(debug, filename=None):
    """define loglevel and log to file or to std"""
    if filename is None:
        if debug:
            logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG)
        else:
            logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)
    else:
        if debug:
            logging.basicConfig(
                filename=filename, format="%(asctime)s %(message)s", level=logging.DEBUG
            )
        else:
            logging.basicConfig(
                filename=filename, format="%(asctime)s %(message)s", level=logging.INFO
            )


def __generate_random_username__(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


def __generate_random_password__(length):
    letters = string.ascii_letters + string.digits
    return "".join(random.choice(letters) for _ in range(length))


def __generate_random_email__(length):
    letters = string.ascii_lowercase
    adress_name = "".join(random.choice(letters) for _ in range(length))
    return f"{adress_name}@geonode-benchmark.org"


def generate_user_file():
    logging.info("Generating users ...")

    num_of_users_to_create = 500

    user_data = []
    used_usernames = set()
    while len(user_data) < num_of_users_to_create:
        username = __generate_random_email__(12)
        while username in used_usernames:
            username = __generate_random_email__(12)
        password = "12345678"  # __generate_random_password__(8)
        user_data.append(f"{username}:{password}")
        used_usernames.add(username)

    logging.info(
        f"writing random credentials of {num_of_users_to_create} users to {USER_DATA_LOCATION} ..."
    )
    with open(USER_DATA_LOCATION, "w") as f:
        f.write("\n".join(user_data))


def create_users_in_geonode():
    logging.info("Creating users in geonode ...")

    with open(USER_DATA_LOCATION, "r") as f:
        user_data = f.read().splitlines()

    gn_conf = gnConf.from_env_vars()
    for user in user_data:
        username, password = user.split(":")

        # filter = {"username": username}
        # users = gnUsers(gn_conf).list(filter=filter)
        # if len(users) != 1:
        logging.debug(f"creating user {username} ...")
        json_user_description = {
            "username": username,
            "password": password,
            "email": username,
        }
        gnUsers(gn_conf).create(json_content=json_user_description)
        # else:
        # logging.debug(f"user {username} already exists ...")

    logging.info("Finished creating users in geonode ...")


def generate_datasets():
    logging.info("Generating datasets ...")
    datasets_list = list(gds.data.flatten().keys())

    size_datasets = []
    for u in range(len(datasets_list)):
        dataset = gpd.read_file(gds.get_path(datasets_list[u]))
        if not isinstance(dataset, gpd.geodataframe.GeoDataFrame):
            continue
        dataset.to_file("./datasets/" + str(u) + ".geojson", driver="GeoJSON")
        # Size in MegaBytes
        size_datasets.append(
            os.stat("./datasets/" + str(u) + ".geojson").st_size / (1024 * 1024)
        )
    logging.info(f"Total size of generated datasets: {sum(size_datasets)} MB")


def upload_datasets_into_geonode():
    logging.info(
        "Uploading datasets into geonode (requires to run --create-users-in-geonode before)..."
    )

    # number of datasts to upload into geonode
    number_of_datasets = 100

    try:
        gn_conf = gnConf.from_env_vars()
        geonode_datasets = gnDatasets(env=gn_conf).list(
            page_size=(number_of_datasets * 2)
        )
        uploaded_datasets = len(geonode_datasets)
        logging.info(f"already found ({uploaded_datasets}) datasets in geonode ...")
    except:
        url = gn_conf.url
        logging.error(f"could not reach geonode at {url}...")
        sys.exit(1)

    datasets = glob.glob(f"{DATASET_LOCATION}/*.geojson")
    while uploaded_datasets < number_of_datasets:
        for dataset in datasets:
            if uploaded_datasets >= number_of_datasets:
                logging.info("maximum number of datasets reached ...")
                return

            logging.debug("Uploading dataset: " + dataset)
            dataset_location = dataset
            gnDatasets(env=gn_conf).upload(file_path=Path(dataset_location))
            uploaded_datasets += 1
            time.sleep(2)
    logging.info("finished uploading datasets into geonode ...")


def delete_all_datasets():
    logging.info("Deleting all datasets ...")
    gn_conf = gnConf.from_env_vars()
    geonode_datasets = gnDatasets(env=gn_conf).list(page_size=(1000))

    for dataset in geonode_datasets:
        logging.debug("deleting dataset: " + dataset["title"])
        gnDatasets(env=gn_conf).delete(pk=dataset["pk"])


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--generate-user-file",
        dest="generate_user_file",
        action="store_true",
        help="generate file with random user credentials in (datsets/users.txt) ...",
    )

    group.add_argument(
        "--create-users-in-geonode",
        dest="create_users_in_geonode",
        action="store_true",
        help="create users in geonode using env variables, like in geonodectl (GEONODE_API_BASIC_AUTH: dXNlcjpwYXNzd29yZA== # you can generate this string like: echo -n user:password | base64)...",
    )

    group.add_argument(
        "--generate-datasets",
        dest="generate_datasets",
        action="store_true",
        help="generate datasets ...",
    )

    group.add_argument(
        "--upload-dataset-into-geonode",
        dest="upload_datasets_into_geonode",
        action="store_true",
        help="create datasets in geonode using env variables, like in geonodectl (GEONODE_API_BASIC_AUTH: dXNlcjpwYXNzd29yZA== # you can generate this string like: echo -n user:password | base64)...",
    )

    group.add_argument(
        "--delete-all-datasets",
        dest="delete_all_datastets",
        action="store_true",
        help="delete all datasets from geonode instance (all ALL!!!), like in geonodectl (GEONODE_API_BASIC_AUTH: dXNlcjpwYXNzd29yZA== # you can generate this string like: echo -n user:password | base64)...",
    )

    # logging
    parser.add_argument(
        "-l",
        "--log",
        help="Redirect logs to a given file in addition to the console.",
        metavar="",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose logging"
    )

    args = parser.parse_args()
    debug = False
    if args.verbose:
        debug = True

    if args.log:
        logfile = args.log
        configure_logging(debug, logfile)
    else:
        configure_logging(debug)
        logging.debug("debug mode enabled")

    if args.generate_user_file:
        generate_user_file()
    elif args.create_users_in_geonode:
        create_users_in_geonode()
    elif args.generate_datasets:
        generate_datasets()
    elif args.upload_datasets_into_geonode:
        upload_datasets_into_geonode()
    elif args.delete_all_datastets:
        delete_all_datastets()
    else:
        raise SystemExit(f"unexpected command ...")


if __name__ == "__main__":
    main()
