
from locust import HttpUser, run_single_user, task

from utils import __generate_random_title__, __pick_random_user__, __pick_random_dataset__,__get_random_user_auth_header__

class PycswLoadTest(HttpUser):

    def on_start(self):
        self.headers = __get_random_user_auth_header__()
      
      
    def __get_dataset_url_from_links_type_by_extensions__(dataset, extension):
        for link in dataset["links"]:
            if link["extension"] == extension:
                return link["url"]
        
    @task
    def get_metadata_xml(self):
      url = self.__get_dataset_url_from_links_type_by_extensions__(dataset=__pick_random_dataset__(), extension="xml")
      self.client.get(f"/catalogue/#/dataset/{pk}")


if __name__ == "__main__":
    run_single_user(PycswLoadTest)
