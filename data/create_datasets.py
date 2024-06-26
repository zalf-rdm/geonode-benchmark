import geopandas as gpd
import geodatasets as gds

datasets_list = list(gds.data.flatten().keys())
print(len(datasets_names))

for u in range(len(datasets_list)):
    dataset = gpd.read_file(gds.get_path(datasets_list[u]))
    dataset.to_file("./datasets/" + str(u) + ".shp")
