import geopandas as gpd
import geodatasets as gds
import os

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

