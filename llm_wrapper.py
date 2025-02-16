import csv
import openai

FILENAME = "zoning_atlas.csv"

DESCRIPTIONS = ['Industrial buildings and structures', 'Single-family buildings', \
                'Multifamily structures: Two Units', 'Residential buildings', \
                'Electric lines, phone and cable lines, etc.', 'Electric substation and distribution facility', \
                'Churches, synagogues, temples, mosques, etc.', 'Store or shop building', 'Multifamily structures', \
                'Commercial buildings and other specialized structures', 'Multifamily structures: Three Units', \
                'Office or store building with residence on top', 'Office or bank building', 'School or university buildings', \
                'Cemetery, monument, tombstone, or mausoleum']