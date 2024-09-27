
import random

from locust import run_single_user, task, between

from utils import GenodeBenchmarkHttpUser

class GeoserverLoadTest(GenodeBenchmarkHttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        # TODO admin:geoserver
        self.client.headers = {"Authorization": "Basic YWRtaW46Z2Vvc2VydmVy"}

    @task(7)
    def get_about(self):
        r = self.client.get("/geoserver/rest/about/version.xml")


    @task(4)
    def get_list_all_layers(self):
        r = self.client.get("/geoserver/rest/layers.json")

    @task(4)
    def get_geodata_workspace(self):
        """
        Task to test the geoserver rest api by retrieving the
        geonode/geodata datastore.
        """
        r_workspaces = self.client.get("/geoserver/rest/workspaces/geonode/datastores/geodata.json")


    @task(5)
    def get_random_featuretype(self):
        r_featuretypes = self.client.get("/geoserver/rest/workspaces/geonode/datastores/geodata/featuretypes.json")
        featuretypes = r_featuretypes.json()['featureTypes']['featureType']

        if len(featuretypes) > 0:
            i = random.randint(0, len(featuretypes) - 1)
            featuretype = featuretypes[i]
            r_featuretype = self.client.get(f"/geoserver/rest/workspaces/geonode/datastores/geodata/featuretypes/{featuretype['name']}.json")

    ###################
    # WFS interaction #
    ###################
    # https://github.com/geopython/OWSLib/tree/master/examples

    # WFS_DOWNLOAD_FORMATS = ["excel","excel2007", "kml", "shp", "csv"]
    
    # @task
    # def wfs_download_in_random_format(self):
    #     r_featuretypes = self.client.get("/geoserver/rest/workspaces/geonode/datastores/geodata/featuretypes.json")
    #     featuretypes = r_featuretypes.json()['featureTypes']['featureType']
        
    #     if len(featuretypes) > 0:
    #         i = random.randint(0, len(featuretypes) - 1)
    #         featuretype = featuretypes[i]
    #         {featuretype['name']}

    ###################
    # WMS interaction #
    ###################