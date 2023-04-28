# Data Sanitizer
# Version: 0.1
# Created by Sergio Madrigal
# ------


# Import values from json
import json
import sys


def array_to_string(textArray):
    result = ""
    # Go through the array
    for element in textArray:
        # Need to extract the text
        if (element[-1] == "." or element[-1] == ":"):
            result = result + element + "\r\n\r\n"
        else:
            if (element[0] == "—"):
                result = result + "\r\n\r\n" + element
            else:
                result = result + element

    return result


def generate_data(dataBase):
    # Get the elements
    for element in dataBase:
        newText = array_to_string(element["leyenda"])
        element["leyenda"] = newText
        element["featured"] = False
    return dataBase


# Code
with open(sys.argv[1], 'r') as file:
    db = json.load(file)

dataBase = generate_data(db)

print(dataBase[0]["leyenda"])

with open("./db_updated.json", "w") as file:
    json.dump(dataBase, file)
