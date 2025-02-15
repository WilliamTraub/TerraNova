import csv

FILENAME = "housing.csv"

def read_csv(filename, skip = 1):
    data = []
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile)
        for _ in range(skip):
            next(csvfile)
        for row in csvfile:
            data.append(row)
    return data

import pandas as pd

# Example: Retrieve property tax parcels data
url = "https://maps.massgis.digital.mass.gov/server/rest/services/Property_Tax_Parcels/FeatureServer/0/query?where=1%3D1&outFields=*&f=geojson"

# Read the JSON and convert to CSV
df = pd.read_json(url)
df.to_csv("property_tax_parcels.csv", index=False)

print(df)