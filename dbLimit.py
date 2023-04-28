# This is a program wich limits the number of entries of a json
#
# The json file is passed as a parameter
# /py dbLimit.py /file.json <number>
#
# The json file is directly imported here and then it will only add
# the first n elements to a new db
#
# This is for currently limiting the amount of data in the database to work with

import json
import sys


def limitDb(value, n):
    return (value[0:n])


with open(sys.argv[1], 'r') as file:
    db = json.load(file)

result = limitDb(db, int(sys.argv[2]))

with open('./dbLimited.json', 'w') as file:
    json.dump(result, file)
