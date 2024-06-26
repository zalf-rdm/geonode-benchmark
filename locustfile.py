from locust import task, run_single_user
from locust import FastHttpUser


class GeonodeLoadTest(FastHttpUser):
    host = "http://https://repository.zalf.de/"
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
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=fQ4TfibLLQAW6vBSGnft7oySfQ80QYH2VJBRZPS8gCWJ6zHKOHaUrbfFSA2uswOH; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIllvdSBoYXZlIHNpZ25lZCBvdXQuIl1d:1sMMvm:kfJkVEpkD5Bt5lNRO5A81WGYi6g2MjKINL2dnuJCGEU; sessionid=1a2am9diab3e6n07ek325o7iaw6e3a6j",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.de",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=fQ4TfibLLQAW6vBSGnft7oySfQ80QYH2VJBRZPS8gCWJ6zHKOHaUrbfFSA2uswOH; sessionid=1a2am9diab3e6n07ek325o7iaw6e3a6j",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:28:27 GMT",
                "If-None-Match": '"667571eb-47e"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.deaccount/login/?next=%2F",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/account/login/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Content-Length": "120",
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": "csrftoken=fQ4TfibLLQAW6vBSGnft7oySfQ80QYH2VJBRZPS8gCWJ6zHKOHaUrbfFSA2uswOH; sessionid=1a2am9diab3e6n07ek325o7iaw6e3a6j",
                "Host": "localhost:8000",
                "Origin": "http://localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.deaccount/login/?next=%2F",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            data="csrfmiddlewaretoken=XYydtUptA3DjmvmXooGQvrE8aOA4nhhKDR5bdr6Q5PZ6mzsPwIBhPelVNyuyZPop&login=admin&password=admin&next=%2F",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.deaccount/login/?next=%2F",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.de",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:28:27 GMT",
                "If-None-Match": '"667571eb-47e"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.de",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/configs/localConfig.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:34 GMT",
                "If-None-Match": '"667573d2-224b3"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.de",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/o/v4/userinfo",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.de",
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
            "/api/v2/users/1000",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.de",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/ms-translations/data.en-US.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:35 GMT",
                "If-None-Match": '"667573d3-2fbd2"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.de",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/gn-translations/data.en-US.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:35 GMT",
                "If-None-Match": '"667573d3-4565"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.de",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources?include[]=executions&filter%7Bmetadata_only%7D=false&page=1&page_size=24",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.de",
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
            "/api/v2/resources?page_size=3&page=1&filter%7Bfeatured%7D=true",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.de",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/catalogue/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.de",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:28:27 GMT",
                "If-None-Match": '"667571eb-47e"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/configs/localConfig.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:34 GMT",
                "If-None-Match": '"667573d2-224b3"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/o/v4/userinfo",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
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
            "/api/v2/users/1000",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/extensions/index.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:35 GMT",
                "If-None-Match": '"667573d3-3"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/ms-translations/data.en-US.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:35 GMT",
                "If-None-Match": '"667573d3-2fbd2"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/gn-translations/data.en-US.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:35 GMT",
                "If-None-Match": '"667573d3-4565"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/?url=http%3A%2F%2Flocalhost%3A8080%2Fgeoserver%2Fpdf%2Finfo.json%3Faccess_token%3DNXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/datasets/1",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
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
            "/api/v2/resources?include[]=executions&filter%7Bmetadata_only%7D=false&page=1&page_size=24",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
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
            "/api/v2/datasets/1",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/datasets/geonode:gis_osm_adminareas_a_07_1/embed?config=dataset_preview",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "iframe",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources/1/linked_resources?page=1&page_size=99999",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
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
            "/api/v2/",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.dedatasets/geonode:gis_osm_adminareas_a_07_1/embed?config=dataset_preview",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/configs/localConfig.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:34 GMT",
                "If-None-Match": '"667573d2-224b3"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.dedatasets/geonode:gis_osm_adminareas_a_07_1/embed?config=dataset_preview",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/o/v4/userinfo",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.dedatasets/geonode:gis_osm_adminareas_a_07_1/embed?config=dataset_preview",
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
            "/api/v2/users/1000",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.dedatasets/geonode:gis_osm_adminareas_a_07_1/embed?config=dataset_preview",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/extensions/index.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:35 GMT",
                "If-None-Match": '"667573d3-3"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.dedatasets/geonode:gis_osm_adminareas_a_07_1/embed?config=dataset_preview",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/ms-translations/data.en-US.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:35 GMT",
                "If-None-Match": '"667573d3-2fbd2"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.dedatasets/geonode:gis_osm_adminareas_a_07_1/embed?config=dataset_preview",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/gn-translations/data.en-US.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:35 GMT",
                "If-None-Match": '"667573d3-4565"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.dedatasets/geonode:gis_osm_adminareas_a_07_1/embed?config=dataset_preview",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/?url=http%3A%2F%2Flocalhost%3A8080%2Fgeoserver%2Fpdf%2Finfo.json%3Faccess_token%3DNXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.dedatasets/geonode:gis_osm_adminareas_a_07_1/embed?config=dataset_preview",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources/1/permissions",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.dedatasets/geonode:gis_osm_adminareas_a_07_1/embed?config=dataset_preview",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/configs/map.json?v=f19121485946edc9a142602b4b078006f526fbd5&access_token=NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:34 GMT",
                "If-None-Match": '"667573d2-326"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.dedatasets/geonode:gis_osm_adminareas_a_07_1/embed?config=dataset_preview",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/datasets/1",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.dedatasets/geonode:gis_osm_adminareas_a_07_1/embed?config=dataset_preview",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/api/v2/datasets?page_size=1&filter%7Balternate.in%7D[]=geonode:gis_osm_adminareas_a_07_1",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.dedatasets/geonode:gis_osm_adminareas_a_07_1/embed?config=dataset_preview",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:28:27 GMT",
                "If-None-Match": '"667571eb-47e"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources/resource_types",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
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
            "/api/v2/resources/1/permissions",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/configs/map.json?v=f19121485946edc9a142602b4b078006f526fbd5&access_token=NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:34 GMT",
                "If-None-Match": '"667573d2-326"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/datasets/1",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
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
            "/api/v2/datasets?page_size=1&filter%7Balternate.in%7D[]=geonode:gis_osm_adminareas_a_07_1",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
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
            "/api/v2/resources/1/linked_resources?page=1&page_size=99999",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://b.tile.openstreetmap.org/11/1101/685.png",
            headers={
                "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-GB,en;q=0.9",
                "if-none-match": '"d8e3cacd5f09b1b342ddcf275a78adaf"',
                "origin": "http://localhost:8000",
                "priority": "u=4, i",
                "sec-fetch-dest": "image",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://c.tile.openstreetmap.org/11/1103/685.png",
            headers={
                "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-GB,en;q=0.9",
                "if-none-match": '"8c1e0b885c181dd9fb9cd1ee0c9945ba"',
                "origin": "http://localhost:8000",
                "priority": "u=4, i",
                "sec-fetch-dest": "image",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://a.tile.openstreetmap.org/11/1101/683.png",
            headers={
                "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-GB,en;q=0.9",
                "if-none-match": '"72429e899872cf493c78ed4698500454"',
                "origin": "http://localhost:8000",
                "priority": "u=4, i",
                "sec-fetch-dest": "image",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://b.tile.openstreetmap.org/11/1100/683.png",
            headers={
                "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-GB,en;q=0.9",
                "if-none-match": '"43275e3bbd9125b64d4b8f022ec6981e"',
                "origin": "http://localhost:8000",
                "priority": "u=4, i",
                "sec-fetch-dest": "image",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://a.tile.openstreetmap.org/11/1104/686.png",
            headers={
                "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-GB,en;q=0.9",
                "if-none-match": '"6380636bca57b7f1bb03b6f636bc9af7"',
                "origin": "http://localhost:8000",
                "priority": "u=4, i",
                "sec-fetch-dest": "image",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/datasets/geonode_data:geonode:gis_osm_adminareas_a_07_1/metadata_detail",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgYWRtaW4uIl1d:1sMMvz:PHGIyQm96XDuSSJZXEci1G2qZUbMVnpH_-tykNn09go; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:28:27 GMT",
                "If-None-Match": '"667571eb-47e"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.dedatasets/geonode_data:geonode:gis_osm_adminareas_a_07_1/metadata_detail",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/catalogue/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.de",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:28:27 GMT",
                "If-None-Match": '"667571eb-47e"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/configs/localConfig.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:34 GMT",
                "If-None-Match": '"667573d2-224b3"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/o/v4/userinfo",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
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
            "/api/v2/users/1000",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/extensions/index.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:35 GMT",
                "If-None-Match": '"667573d3-3"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/ms-translations/data.en-US.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:35 GMT",
                "If-None-Match": '"667573d3-2fbd2"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/gn-translations/data.en-US.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:35 GMT",
                "If-None-Match": '"667573d3-4565"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/?url=http%3A%2F%2Flocalhost%3A8080%2Fgeoserver%2Fpdf%2Finfo.json%3Faccess_token%3DNXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources/resource_types",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
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
            "/api/v2/resources/1/permissions",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/configs/map.json?v=f19121485946edc9a142602b4b078006f526fbd5&access_token=NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:34 GMT",
                "If-None-Match": '"667573d2-326"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/datasets/1",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
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
            "/api/v2/datasets?page_size=1&filter%7Balternate.in%7D[]=geonode:gis_osm_adminareas_a_07_1",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
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
            "/api/v2/resources/1/linked_resources?page=1&page_size=99999",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://b.tile.openstreetmap.org/11/1101/685.png",
            headers={
                "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-GB,en;q=0.9",
                "if-none-match": '"d8e3cacd5f09b1b342ddcf275a78adaf"',
                "origin": "http://localhost:8000",
                "priority": "u=4, i",
                "sec-fetch-dest": "image",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://c.tile.openstreetmap.org/11/1103/685.png",
            headers={
                "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-GB,en;q=0.9",
                "if-none-match": '"8c1e0b885c181dd9fb9cd1ee0c9945ba"',
                "origin": "http://localhost:8000",
                "priority": "u=4, i",
                "sec-fetch-dest": "image",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://a.tile.openstreetmap.org/11/1101/683.png",
            headers={
                "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-GB,en;q=0.9",
                "if-none-match": '"72429e899872cf493c78ed4698500454"',
                "origin": "http://localhost:8000",
                "priority": "u=4, i",
                "sec-fetch-dest": "image",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://b.tile.openstreetmap.org/11/1100/683.png",
            headers={
                "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-GB,en;q=0.9",
                "if-none-match": '"43275e3bbd9125b64d4b8f022ec6981e"',
                "origin": "http://localhost:8000",
                "priority": "u=4, i",
                "sec-fetch-dest": "image",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://a.tile.openstreetmap.org/11/1104/686.png",
            headers={
                "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-GB,en;q=0.9",
                "if-none-match": '"6380636bca57b7f1bb03b6f636bc9af7"',
                "origin": "http://localhost:8000",
                "priority": "u=4, i",
                "sec-fetch-dest": "image",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/datasets/geonode:gis_osm_adminareas_a_07_1/dataset_download",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:28:27 GMT",
                "If-None-Match": '"667571eb-47e"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources?include[]=executions&filter%7Bmetadata_only%7D=false&page=1&page_size=24",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
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
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:28:27 GMT",
                "If-None-Match": '"667571eb-47e"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
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
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
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
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
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
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.rest(
            "POST",
            "/api/v2/uploads/upload",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Content-Length": "4743719",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Origin": "http://localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
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
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
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
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
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
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
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
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
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
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:28:27 GMT",
                "If-None-Match": '"667571eb-47e"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources?include[]=executions&filter%7Bmetadata_only%7D=false&page=1&page_size=24",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.rest(
            "DELETE",
            "/api/v2/resources/6/delete",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Origin": "http://localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
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
            "/api/v2/resource-service/execution-status/b8a8b10a-b789-4939-a6d7-5905d016ba2d",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Authorization": "Bearer NXEp1IkxiZygAh5tKWlXC2cOpyPL0z",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/account/logout/?next=/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.decatalogue/",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:28:27 GMT",
                "If-None-Match": '"667571eb-47e"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.deaccount/logout/?next=/",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/account/logout/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Content-Length": "84",
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; sessionid=ybv5uq6wqy0xft0kf4ymlqsli5q9gtot",
                "Host": "localhost:8000",
                "Origin": "http://localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.deaccount/logout/?next=/",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            data="csrfmiddlewaretoken=gzjZOaSZnMNJZVD3rjvrWvGRbAeMIMzDJhC0oAs7H8xXqV76WxWShWTPHzm7CQfQ",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIllvdSBoYXZlIHNpZ25lZCBvdXQuIl1d:1sMMxe:L9NpKRb8f2KrGoJFqtBoG-2ntVUmeDLy2WFy8G5pSrw",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.deaccount/logout/?next=/",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIllvdSBoYXZlIHNpZ25lZCBvdXQuIl1d:1sMMxe:L9NpKRb8f2KrGoJFqtBoG-2ntVUmeDLy2WFy8G5pSrw; sessionid=dbhdrpufxmvda6wxcw9qpt96o9vrmqd2",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.de",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/geonode/img/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIllvdSBoYXZlIHNpZ25lZCBvdXQuIl1d:1sMMxe:L9NpKRb8f2KrGoJFqtBoG-2ntVUmeDLy2WFy8G5pSrw; sessionid=dbhdrpufxmvda6wxcw9qpt96o9vrmqd2",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:28:27 GMT",
                "If-None-Match": '"667571eb-47e"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.de",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/configs/localConfig.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIllvdSBoYXZlIHNpZ25lZCBvdXQuIl1d:1sMMxe:L9NpKRb8f2KrGoJFqtBoG-2ntVUmeDLy2WFy8G5pSrw; sessionid=dbhdrpufxmvda6wxcw9qpt96o9vrmqd2",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:34 GMT",
                "If-None-Match": '"667573d2-224b3"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.de",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/o/v4/userinfo",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIllvdSBoYXZlIHNpZ25lZCBvdXQuIl1d:1sMMxe:L9NpKRb8f2KrGoJFqtBoG-2ntVUmeDLy2WFy8G5pSrw; sessionid=dbhdrpufxmvda6wxcw9qpt96o9vrmqd2",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.de",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/ms-translations/data.en-US.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIllvdSBoYXZlIHNpZ25lZCBvdXQuIl1d:1sMMxe:L9NpKRb8f2KrGoJFqtBoG-2ntVUmeDLy2WFy8G5pSrw; sessionid=dbhdrpufxmvda6wxcw9qpt96o9vrmqd2",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:35 GMT",
                "If-None-Match": '"667573d3-2fbd2"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.de",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/mapstore/gn-translations/data.en-US.json?v=f19121485946edc9a142602b4b078006f526fbd5",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIllvdSBoYXZlIHNpZ25lZCBvdXQuIl1d:1sMMxe:L9NpKRb8f2KrGoJFqtBoG-2ntVUmeDLy2WFy8G5pSrw; sessionid=dbhdrpufxmvda6wxcw9qpt96o9vrmqd2",
                "Host": "localhost:8000",
                "If-Modified-Since": "Fri, 21 Jun 2024 12:36:35 GMT",
                "If-None-Match": '"667573d3-4565"',
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.de",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/v2/resources?include[]=executions&filter%7Bmetadata_only%7D=false&page=1&page_size=24",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIllvdSBoYXZlIHNpZ25lZCBvdXQuIl1d:1sMMxe:L9NpKRb8f2KrGoJFqtBoG-2ntVUmeDLy2WFy8G5pSrw; sessionid=dbhdrpufxmvda6wxcw9qpt96o9vrmqd2",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.de",
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
            "/api/v2/resources?page_size=3&page=1&filter%7Bfeatured%7D=true",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-GB,en;q=0.9",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIllvdSBoYXZlIHNpZ25lZCBvdXQuIl1d:1sMMxe:L9NpKRb8f2KrGoJFqtBoG-2ntVUmeDLy2WFy8G5pSrw; sessionid=dbhdrpufxmvda6wxcw9qpt96o9vrmqd2",
                "Host": "localhost:8000",
                "Referer": " https://geonode-benchmark.draven.cluster.zalf.de",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-CSRFToken": "twhG0zormRBZfIn5QFW8l33CRjr2awWKWeAHAZYzGdldGIR8lTnzGugAnizn4ACX",
            },
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(GeonodeLoadTest)
