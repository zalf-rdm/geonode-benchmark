import csv
import argparse

import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument(
    "-s", "--source", help="csv file input",dest="csv_file_name", type=str
)
args = parser.parse_args()
df = pd.read_csv(args.csv_file_name)

print(df["Average Response Time"])
plt.figure()
ax = plt.gca()
#ax.set_xlim([0, 100])
ax.set_ylim([0, 8000])
plt.title("Average Response Time")
plt.plot(df["Average Response Time"]) #, df["Min Response Time"])
plt.show()