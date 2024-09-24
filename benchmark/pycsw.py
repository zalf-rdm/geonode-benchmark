
from urllib.parse import urlparse, unquote

from locust import run_single_user, task, between

from utils import GenodeBenchmarkHttpUser

# requires: 
# https://github.com/geopython/OWSLib/blob/master/owslib/csw.py
class PycswLoadTest(GenodeBenchmarkHttpUser):
    wait_time = between(1, 5)

    #outputschema = 'http://www.isotc211.org/2005/gmd'
    lang = 'en-US'
    version = '2.0.2'

    def __get_dataset_url_from_links_type_by_name__(self, dataset, name):
        for link in dataset["links"]:
            if link["name"] == name:
                domain_path = link["url"]
                return urlparse(unquote(domain_path))

    ###################
    # CSW interaction #
    ###################
    @task
    def get_metadata_atom(self):
        domain_path = self.__get_dataset_url_from_links_type_by_name__(
            dataset=self.__pick_random_dataset__(), name="Atom"
        )
        if domain_path is not None:
            self.client.get(domain_path.geturl())
  
    @task
    def get_metadata_dif(self):
        domain_path = self.__get_dataset_url_from_links_type_by_name__(
            dataset=self.__pick_random_dataset__(), name="DIF"
        )
        if domain_path is not None:
            self.client.get(domain_path.geturl())
  
    @task
    def get_metadata_dublin_core(self):
        domain_path = self.__get_dataset_url_from_links_type_by_name__(
            dataset=self.__pick_random_dataset__(), name="Dublin Core"
        )
        if domain_path is not None:
            self.client.get(domain_path.geturl())

    @task
    def get_metadata_dublin_ebrim(self):
        domain_path = self.__get_dataset_url_from_links_type_by_name__(
            dataset=self.__pick_random_dataset__(), name="ebRIM"
        )
        if domain_path is not None:
            self.client.get(domain_path.geturl())

    @task
    def get_metadata_dublin_fgdc(self):
        domain_path = self.__get_dataset_url_from_links_type_by_name__(
            dataset=self.__pick_random_dataset__(), name="FGDC"
        )
        if domain_path is not None:
            self.client.get(domain_path.geturl())

    @task
    def get_metadata_dublin_iso(self):
        domain_path = self.__get_dataset_url_from_links_type_by_name__(
            dataset=self.__pick_random_dataset__(), name="ISO"
        )
        if domain_path is not None:
            self.client.get(domain_path.geturl())

if __name__ == "__main__":
    run_single_user(PycswLoadTest)
