from locust import task, run_single_user
from locust import FastHttpUser


class GeonodeLoadTest(FastHttpUser):
    host = "http://geonode-benchmark.draven.cluster.zalf.de"
    default_headers = {
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/account/login/?next=%2F",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/account/login/",
            data="csrfmiddlewaretoken=XYydtUptA3DjmvmXooGQvrE8aOA4nhhKDR5bdr6Q5PZ6mzsPwIBhPelVNyuyZPop&login=admin&password=admin&next=%2F",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/configs/localConfig.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/o/v4/userinfo",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/users/1000",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/ms-translations/data.en-US.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/gn-translations/data.en-US.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources?include[]=executions&filter%7Bmetadata_only%7D=false&page=1&page_size=24",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources?page_size=3&page=1&filter%7Bfeatured%7D=true",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/catalogue/",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/configs/localConfig.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/o/v4/userinfo",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/users/1000",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/extensions/index.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/ms-translations/data.en-US.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/gn-translations/data.en-US.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/?url=http%3A%2F%2Flocalhost%3A8080%2Fgeoserver%2Fpdf%2Finfo.json%3Faccess_token%3DNXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/datasets/1",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources?include[]=executions&filter%7Bmetadata_only%7D=false&page=1&page_size=24",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/datasets/1",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/datasets/geonode:gis_osm_adminareas_a_07_1/embed?config=dataset_preview",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources/1/linked_resources?page=1&page_size=99999",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/configs/localConfig.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/o/v4/userinfo",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/users/1000",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/extensions/index.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/ms-translations/data.en-US.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/gn-translations/data.en-US.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/?url=http%3A%2F%2Flocalhost%3A8080%2Fgeoserver%2Fpdf%2Finfo.json%3Faccess_token%3DNXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources/1/permissions",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/configs/map.json?v=f19121485946edc9a142602b4b078006f526fbd5&access_token=NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/datasets/1",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/api/v2/datasets?page_size=1&filter%7Balternate.in%7D[]=geonode:gis_osm_adminareas_a_07_1",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources/resource_types",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources/1/permissions",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/configs/map.json?v=f19121485946edc9a142602b4b078006f526fbd5&access_token=NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/datasets/1",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/datasets?page_size=1&filter%7Balternate.in%7D[]=geonode:gis_osm_adminareas_a_07_1",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources/1/linked_resources?page=1&page_size=99999",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://b.tile.openstreetmap.org/11/1101/685.png",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://c.tile.openstreetmap.org/11/1103/685.png",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://a.tile.openstreetmap.org/11/1101/683.png",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://b.tile.openstreetmap.org/11/1100/683.png",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://a.tile.openstreetmap.org/11/1104/686.png",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/datasets/geonode_data:geonode:gis_osm_adminareas_a_07_1/metadata_detail",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/catalogue/",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/configs/localConfig.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/o/v4/userinfo",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/users/1000",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/extensions/index.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/ms-translations/data.en-US.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/gn-translations/data.en-US.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/?url=http%3A%2F%2Flocalhost%3A8080%2Fgeoserver%2Fpdf%2Finfo.json%3Faccess_token%3DNXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources/resource_types",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources/1/permissions",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/configs/map.json?v=f19121485946edc9a142602b4b078006f526fbd5&access_token=NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/datasets/1",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/datasets?page_size=1&filter%7Balternate.in%7D[]=geonode:gis_osm_adminareas_a_07_1",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources/1/linked_resources?page=1&page_size=99999",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://b.tile.openstreetmap.org/11/1101/685.png",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://c.tile.openstreetmap.org/11/1103/685.png",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://a.tile.openstreetmap.org/11/1101/683.png",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://b.tile.openstreetmap.org/11/1100/683.png",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://a.tile.openstreetmap.org/11/1104/686.png",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/datasets/geonode:gis_osm_adminareas_a_07_1/dataset_download",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources?include[]=executions&filter%7Bmetadata_only%7D=false&page=1&page_size=24",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/executionrequest?filter%7Baction%7D=import&filter%7Bsource%7D=upload&page=1&page_size=99999",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/executionrequest?filter%7Baction%7D=import&filter%7Bsource%7D=upload&page=1&page_size=99999",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": "http://localhost:8000/catalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/executionrequest?filter%7Baction%7D=import&filter%7Bsource%7D=upload&page=1&page_size=99999",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/executionrequest?filter%7Baction%7D=import&filter%7Bsource%7D=upload&page=1&page_size=99999",
        ) as resp:
            pass
        with self.rest(
            "POST",
            "/api/v2/uploads/upload",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/executionrequest?filter%7Baction%7D=import&filter%7Bsource%7D=upload&page=1&page_size=99999",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/executionrequest?filter%7Baction%7D=import&filter%7Bsource%7D=upload&page=1&page_size=99999",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/executionrequest?filter%7Baction%7D=import&filter%7Bsource%7D=upload&page=1&page_size=99999",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/executionrequest?filter%7Baction%7D=import&filter%7Bsource%7D=upload&page=1&page_size=99999",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/executionrequest?filter%7Baction%7D=import&filter%7Bsource%7D=upload&page=1&page_size=99999",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources?include[]=executions&filter%7Bmetadata_only%7D=false&page=1&page_size=24",
        ) as resp:
            pass
        with self.rest(
            "DELETE",
            "/api/v2/resources/6/delete",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resource-service/execution-status/b8a8b10a-b789-4939-a6d7-5905d016ba2d",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/account/logout/?next=/",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/account/logout/",
            data="csrfmiddlewaretoken=gzjZOaSZnMNJZVD3rjvrWvGRbAeMIMzDJhC0oAs7H8xXqV76WxWShWTPHzm7CQfQ",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/configs/localConfig.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/o/v4/userinfo",
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/ms-translations/data.en-US.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/gn-translations/data.en-US.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources?include[]=executions&filter%7Bmetadata_only%7D=false&page=1&page_size=24",
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources?page_size=3&page=1&filter%7Bfeatured%7D=true",
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(GeonodeLoadTest)
