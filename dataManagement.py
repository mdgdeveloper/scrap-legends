# Data Manager
# v0.1
#
# Created by Sergio Madrigal

import json
import sys


# Add images in incremental order
def addImages(dataBase):
    for (k, element) in enumerate(dataBase):
        imgBase = str(k+1).zfill(3)
        element["img"] = [f"{imgBase}_01.jpg", f"{imgBase}_02.jpg"]

    return dataBase


# Code
with open(sys.argv[1], 'r') as file:
    db = json.load(file)

dataBase = addImages(db)

# Write File
with open(sys.argv[2], "w") as file:
    json.dump(dataBase, file)
