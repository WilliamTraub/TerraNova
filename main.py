import csv

FILENAME = "ma_suffolk.csv"

def read_csv(filename, skip = 1):
    data = []
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile)
        for _ in range(skip):
            next(csvfile)
        for row in csvfile:
            data.append(row)
    return data

data = read_csv(FILENAME)
print(data)