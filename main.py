import pandas as pd
import csv
from land import Land
import os

path = "/Users/hyjiang/innovaite/data"
FILES = os.listdir(path)

data = [pd.read_csv(os.path.join(path, file)) for file in FILES]
merged_data = pd.concat(data, ignore_index=True)

merged_data.to_csv("data/merged_ma.csv", index=False)

FILENAME = "data/merged_ma.csv"
ATTRIBS = ["zoning_description", "zoning_type", "zoning_subtype", "lbcs_structure_desc", \
           "lat", "lon", "ll_gissqft"]
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
    clean_lands = []
    for land in lands:
        if not land.lbcs_structure_desc == "":
            clean_lands.append(land)
    print(len(clean_lands))

main()