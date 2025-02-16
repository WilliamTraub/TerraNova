import pandas as pd
import csv
from land import Land

# FILES = ["data/ma_essex.csv", "data/ma_middlesex.csv", \
#          "data/ma_norfolk.csv", "data/ma_suffolk.csv"]

# data = [pd.read_csv(file) for file in FILES]
# merged_data = pd.concat(data, ignore_index=True)

# merged_data.to_csv("data/merged_ma.csv", index=False)

FILENAME = "data/merged_ma.csv"
ATTRIBS = ["zoning_description", "zoning_type", "zoning_subtype", \
           "landval", "lat", "lon", "sqft"]
CITYCENTER = Land(lat = 42.3394, lon = -71.0940)

def read_csv(filename):
    data = []
    with open(filename, "r") as infile:
        csvfile = csv.DictReader(infile)
        for row in csvfile:
            data.append(row)
    return data

def clean_data(data, keys):
    clean_lst = []
    for dct in data:
        clean_dct = {}
        for key in keys:
            clean_dct[key] = dct[key]
        clean_lst.append(clean_dct)
    return clean_lst

def create_lands(data):
    lands = []
    for row in data:
        land = Land(**row)
        land.add_haversine(CITYCENTER)
        lands.append(land)
    return lands

def main():
    data = read_csv(FILENAME)
    data = clean_data(data, ATTRIBS)
    lands = create_lands(data)

main()