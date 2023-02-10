import json

f = open("legscrapper/test.json", "r", encoding='utf-8', errors='ignore')
data = f.read()
dataList = json.loads(data)
count = 0

for value in dataList:
    print(value["title"])
    count += 1

print(count)
