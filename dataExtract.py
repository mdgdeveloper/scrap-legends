# Data Extractor for Testing
# Created by Sergio Madrigal

#  Main goals of the document
#  [ ] Extract 20 entries for testing purposes
#  [ ] List the titles of the 20 entries together with the location (in case we need the update we need to identify the ones which missing data)


import json
import sys


def dataExtract(db):
    return db[0:19]


# Open file
with open(sys.argv[1], 'r') as file:
    db = json.load(file)

# Create Last
last = dataExtract(db)

# List file
for element in last:
    print(f'{element["title"]},{element["province"]}')

# Write File
with open(sys.argv[2], "w") as file:
    json.dump(last, file)
