import os
import wget
import json

f = open("values.json", "r", encoding='utf-8', errors='ignore')
data = f.read()
dataList = json.loads(data)

base_url = 'https://www.descubreleyendas.es'


count = 0
for value in dataList:
    image = value["img"][0][2:]
    image_unique = value["img"][0][17:]
    url = base_url + image
    save_as = "H:\data\images\\" + str(count) + "_" + image_unique
    print(save_as)
    count += 1
    try:
        wget.download(url, out=save_as)
    except:
        print("Error")
