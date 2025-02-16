import csv
from land import Land

SUFFOLK = "ma_suffolk.csv"
NORFOLK = "ma_norfolk.csv"
MIDDLESEX = "ma_middlesex.csv"
ESSEX = "ma_essex.csv"
LST = [SUFFOLK, NORFOLK, MIDDLESEX, ESSEX]
CITYCENTER = Land(42.3394, -71.0940)

def read_csv(filename):
    data = []
    with open(filename, "r") as infile:
        data = []
        csvfile = csv.DictReader(infile)
        for row in csvfile:
            data.append(row)
    return data

def get_val(dct, key):
    return [row[key] for row in dct]

def float_2d(lst):
    for row in lst:
        for i in range(len(row)):
            row[i] = float(row[i])

def lands(lat, lon, land_val, sqft, zoning_desc_vals, zoning_type_vals, zoning_sub_vals):
    land_lst = []
    for i in range(len(lat)):
        land = Land(lat[i], lon[i], land_val[i], sqft[i], zoning_desc_vals[i], zoning_type_vals[i], zoning_sub_vals[i])
        land_lst.append(land)
    return land_lst

def main():
    data = read_csv(FILENAME)
    lat_vals = get_val(data, "lat")
    lon_vals = get_val(data, "lon")
    land_vals = get_val(data, "landval")
    sqft_vals = get_val(data, "sqft")
    zoning_desc_vals = get_val(data, "zoning_description")
    zoning_type_vals = get_val(data, "zoning_type")
    zoning_sub_vals = get_val(data, "zoning_subtype")

    float_2d([lat_vals, lon_vals, land_vals, sqft_vals])

    land_lst = lands(lat_vals, lon_vals, land_vals)
    for land in land_lst:
        land.add_haversine(CITYCENTER)
        print(land)

main()