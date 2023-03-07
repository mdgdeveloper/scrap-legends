from dataSanitize import *
import json
import time


# Opening JSON file
f = open('values.json', "r", encoding='utf-8')

# returns JSON object as
# a dictionary
json_file = json.load(f)

# Iterating through the json
# list
finalResult = []
for element in json_file:
    if (element["location"]):
        # print(element["location"].lower())
        locationInfo = locationData(element["location"].lower())
        element["province"] = locationInfo[0]
        element["community"] = locationInfo[1]
        print(f"Municipality: {element['location']}")
        print(f"Province: {element['province']}")
        print(f"Community: {element['community']}")
        print("----")
    time.sleep(10)
    finalResult.append(element)
# Closing file
f.close()

print(finalResult)
