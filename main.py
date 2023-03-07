import json
from data import *


f = open("values.json", "r", encoding='utf-8', errors='ignore')
data = f.read()
dataList = json.loads(data)
count = 0

result = []

for value in dataList:
    id = count
    title = (sanitizer_title(value))
    author = (sanitizer_author(value))
    location = (sanitizer_location(value))
    events = value["acontecimientos"]
    personajes = sanitizer_characters(value)
    legend = sanitizer_text(value)
    img = sanitizer_img(value, id)
    count += 1
    # Element creation
    element = dict()
    element["id"] = id
    element["title"] = title
    element["author"] = author
    element["location"] = location
    element["events"] = events
    element["characters"] = personajes
    element["img"] = img
    element["legend"] = legend

    # Result
    result.append(element)


final = json.dumps(result, indent=2)

print(final)
