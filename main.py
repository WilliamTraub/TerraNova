import csv

FILENAME = "ma_suffolk.csv"

def read_csv(filename, skip = 1):
    data = []
    with open(filename, "r") as infile:
        data = []
        csvfile = csv.DictReader(filename)
        for row in csvfile:
            data.append(row)
        return data

