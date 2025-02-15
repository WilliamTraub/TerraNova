import csv

FILENAME = "ma_suffolk.csv"

def read_csv(filename, skip = 1):
    data = []
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile)
        next(csvfile)
        for row in csvfile:
            key = row[0]
            values = [val for val in row]
            data[key] = values
    return data

data = read_csv(FILENAME)
for row in data:
    print(row)