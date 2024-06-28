def __pick_random_file__():
    filename = random.choice(os.listdir("./datasets"))
    title = filename.split(".")[0]
    file_definition = "geojson_file"
    file_format = "application/geo+json"
    to_upload = [
        (
            file_definition,
            (title, open(filename, "rb"), file_format),
        ),
    ]
    return to_upload


@task(8)
def dataset_upload(self):
    file = __pick_random_file__()
    self.client.post("/api/v2/uploads/upload", file)
    pass
