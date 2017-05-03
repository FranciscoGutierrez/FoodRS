# -*- coding: UTF-8 -*-
from pymongo import MongoClient
from sklearn.metrics import jaccard_similarity_score
import pprint
import numpy as np

def getProducts(uri):
    # Mongo URI: "mongodb://<user>:<password>@ds161400.mlab.com:61400/healthyfoods"
    client = MongoClient(uri)
    db = client['healthyfoods']
    products = db.products
    print "==== Products Acquired ===="
    return products.find()

# Discover things, explore similar products... not related to user profile.
def similar_products(uri, products):
    client = MongoClient(uri)
    db = client['healthyfoods']
    output = []
    for a in products:
        score = 0.0
        key_a = a["_keywords"]
        table = []
        for b in products:
            key_b   = b["_keywords"]
            key_max = max(len(key_a), len(key_b))
            key_a = key_a + [0]*(key_max - len(key_a))
            key_b = key_b + [0]*(key_max - len(key_b))
            score = jaccard_similarity_score(key_a, key_b)
            if(score < 1.0 and score > 0.5): # and > 0.5 to get the most similar products.
                table.append({"_id": b["_id"], "score": score})# "product": b})
        output.append({"_id": a["_id"], "similarity" : table})
    #pprint.pprint(output)
    result = db.similar.insert_many(output)
    print "done!"
    return 0;

def similarity_test(a,b):
    return jaccard_similarity_score(a,b)

# Based in the products the user usually likes, find healthy alternatives.
def alternative_products(uri, list):
    client = MongoClient(uri)
    db = client['healthyfoods']
    output = []
    for a in products:
        test_a = a["_keywords"]
        table = []
        for b in products:
            test_b = b["_keywords"]
            if len(test_a) > 0 and len(test_b) > 0:
                score = jaccard_similarity_score(test_a, test_b)
            else:
                score = 0.0
            if(score < 1.0): # and > 0.5 to get the most similar products.
                table.append({"_id": b["_id"], "score": score})# "product": b})
        output.append({"_id": test_a, "similarity" : table})
    pprint.pprint(output)
    result = db.alternative.insert_many(output)
    return 0;

def deleteAllSimilar(uri):
    client = MongoClient(uri)
    db = client['healthyfoods']
    result = db.similar.delete_many({})
    return result.deleted_count

def deleteAllAlternative(uri):
    client = MongoClient(uri)
    db = client['healthyfoods']
    result = db.alternative.delete_many({})
    return result.deleted_count
