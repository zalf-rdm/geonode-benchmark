import geopandas as gpd
import geodatasets as gds
import os

datasets_list = list(gds.data.flatten().keys())
print(len(datasets_list))

size_datasets = []
for u in range(len(datasets_list)):
    dataset = gpd.read_file(gds.get_path(datasets_list[u]))
    dataset.to_file("./datasets/" + str(u) + ".geojson", driver="GeoJSON")
    # Size in MegaBytes
    size_datasets.append(
        os.stat("./datasets/" + str(u) + ".geojson").st_size / (1024 * 1024)
    )

gpd.hist(size_datasets)
