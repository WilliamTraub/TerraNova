import csv
import openai

ZONING = "zoning_atlas.csv"

DESCRIPTIONS = ['Industrial buildings and structures', 'Single-family buildings',
                'Multifamily structures: Two Units', 'Residential buildings',
                'Electric lines, phone and cable lines, etc.', 'Electric substation and distribution facility',
                'Churches, synagogues, temples, mosques, etc.', 'Store or shop building', 'Multifamily structures',
                'Commercial buildings and other specialized structures', 'Multifamily structures: Three Units',
                'Office or store building with residence on top', 'Office or bank building', 'School or university buildings',
                'Cemetery, monument, tombstone, or mausoleum']

def read_csv(filename):
    with open(filename, "r", encoding="utf-8", errors="replace") as infile:
        csvfile = csv.DictReader(infile)
        data = []
        for row in csvfile:
            data.append(row)
    return data

print(len(DESCRIPTIONS))