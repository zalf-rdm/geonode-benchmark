
from urllib.parse import urlparse, unquote

from owslib.csw import CatalogueServiceWeb
from locust import run_single_user, task

from utils import GenodeBenchmarkHttpUser

# requires: 
# https://github.com/geopython/OWSLib/blob/master/owslib/csw.py
class PycswLoadTest(GenodeBenchmarkHttpUser):

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
    # @task
    # def get_metadata_atom(self):
    #     url = self.__get_dataset_url_from_links_type_by_name__(
    #         dataset=self.__pick_random_dataset__(), name="Atom"
    #     )
    #     # TODO try from ZALF
    #     c = CatalogueServiceWeb(url, self.lang, self.version)


    

    @task
    def get_metadata_dif(self):
        domain_path = self.__get_dataset_url_from_links_type_by_name__(
            dataset=self.__pick_random_dataset__(), name="DIF"
        )
        breakpoint()
        self.client.get(domain_path.geturl())

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
