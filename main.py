import csv
from land import Land

FILENAME = "ma_suffolk.csv"
CITYCENTER = (42.3394, -71.0940)

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

def generate_tuples(lst1, lst2):
    tuples = []
    for i in range(len(lst1)):
        tuples.append((lst1[i], lst2[i]))
    return tuples

def lands(lat, long, land_val):
    for i in range(len(lat)):
        land = Land(lat[i], long[i], land_val[i])


def main():
    data = read_csv(FILENAME)
    lat_vals = get_val(data, "lat")
    long_vals = get_val(data, "lon")
    land_vals = get_val(data, "landval")
    float_2d([lat_vals, long_vals, land_vals])
    lat_long = generate_tuples(lat_vals, long_vals)
    print(lat_vals)

main()