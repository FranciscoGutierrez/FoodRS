import json
import urllib2
import keys
import csv

from pymongo import MongoClient

client = MongoClient(keys.URI)
db = client['healthyfoods']
products = list(db.products.find())
table = []

for a in products:
    print a["_id"]
    table.append(a["_id"])

with open('eggs.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile,  ['id', 'url'])
    writer.writeheader()
    for id in table:
        url = 'https://world.openfoodfacts.org/api/v0/product/'+id+'.json'
        try:
            resp = json.load(urllib2.urlopen(url))
            writer.writerow({'id': id, 'url': resp["product"]["image_url"]})
        except Exception as e:
            writer.writerow({'id': id, 'url': "demo/d1.png"})
