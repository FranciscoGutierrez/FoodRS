from pymongo import MongoClient
from sklearn.metrics import jaccard_similarity_score
import pprint
import numpy as np

def getProducts(uri):
    # Mongo URI: "mongodb://<user>:<password>@ds161400.mlab.com:61400/healthyfoods"
    client = MongoClient(uri)
    db = client['healthyfoods']
    products = db.products
    return products.find()

# Discover things, explore similar products... not related to user profile.
def similar_products(uri, products):
    client = MongoClient(uri)
    db = client['healthyfoods']
    output = []
    for a in products:
        table = []
        for b in products:
            score = jaccard_similarity_score(a["tags"], b["tags"])
            if(score < 1.0): # and > 0.5 to get the most similar products.
                table.append({"_id": b["_id"], "score": score})# "product": b})
        output.append({"_id": a["_id"], "similarity" : table})
    pprint.pprint(output)
    result = db.similar.insert_many(output)
    return 0;

# Based in the products the user usually likes, find healthy alternatives.
def alternative_products(uri, list):
    client = MongoClient(uri)
    db = client['healthyfoods']
    output = []
    for a in products:
        table = []
        for b in products:
            score = jaccard_similarity_score(a["tags"], b["tags"])
            if(score < 1.0): # and > 0.5 to get the most similar products.
                table.append({"_id": b["_id"], "score": score})# "product": b})
        output.append({"_id": a["_id"], "similarity" : table})
    pprint.pprint(output)
    result = db.alternative.insert_many(output)
    return 0;

def deleteAllSimilar():
    result = db.similar.delete_many({})
    return result.deleted_count

def deleteAllAlternative():
    result = db.alternative.delete_many({})
    return result.deleted_count
