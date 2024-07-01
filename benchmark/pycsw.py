from locust import run_single_user, task

from utils import GenodeBenchmarkHttpUser
from urllib.parse import urlparse, unquote

# requires: 
# https://github.com/geopython/OWSLib/blob/master/owslib/csw.py
class PycswLoadTest(GenodeBenchmarkHttpUser):

    def __get_dataset_url_from_links_type_by_name__(self, dataset, name):
        for link in dataset["links"]:
            if link["name"] == name:
                domain_path = link["url"]
                return urlparse(unquote(domain_path))

    @task
    def get_metadata_atom(self):
        url = self.__get_dataset_url_from_links_type_by_name__(
            dataset=self.__pick_random_dataset__(), name="Atom"
        )
        self.client.get(url.path)


    # @task
    # def get_metadata_dif(self):
    #     domain_path = self.__get_dataset_url_from_links_type_by_name__(
    #         dataset=self.__pick_random_dataset__(), name="DIF"
    #     )
    #     self.client.get(domain_path)

    # @task
    # def get_metadata_dublin_core(self):
    #     domain_path = self.__get_dataset_url_from_links_type_by_name__(
    #         dataset=self.__pick_random_dataset__(), name="Dublin Core"
    #     )
    #     self.client.get(domain_path)

    # @task
    # def get_metadata_dublin_ebrim(self):
    #     domain_path = self.__get_dataset_url_from_links_type_by_name__(
    #         dataset=self.__pick_random_dataset__(), name="ebRIM"
    #     )
    #     self.client.get(domain_path)

    # @task
    # def get_metadata_dublin_fgdc(self):
    #     domain_path = self.__get_dataset_url_from_links_type_by_name__(
    #         dataset=self.__pick_random_dataset__(), name="FGDC"
    #     )
    #     self.client.get(domain_path)

    # @task
    # def get_metadata_dublin_iso(self):
    #     domain_path = self.__get_dataset_url_from_links_type_by_name__(
    #         dataset=self.__pick_random_dataset__(), name="ISO"
    #     )
    #     self.client.get(domain_path)


if __name__ == "__main__":
    run_single_user(PycswLoadTest)
