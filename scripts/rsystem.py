# -*- coding: UTF-8 -*-
from pymongo import MongoClient
from sklearn.metrics import jaccard_similarity_score
import pprint
import numpy as np
import csv

# Mongo URI: "mongodb://<user>:<password>@ds161400.mlab.com:61400/healthyfoods"

def getProducts(uri):
    client = MongoClient(uri)
    db = client['healthyfoods']
    products = db.products
    return products.find()

def getDrinks(uri):
    client = MongoClient(uri)
    db = client['healthyfoods']
    products = db.products
    list = ["en:beverages","en:carbonated-drinks","en:sodas","en:sugared-beverages"]
    return products.find({"categories_tags": { "$in": list }})

def getVeggiesFruits(uri):
    client = MongoClient(uri)
    db = client['healthyfoods']
    products = db.products
    return products.find({"categories_tags": "en:plant-based-foods"})

def getProteins(uri):
    client = MongoClient(uri)
    db = client['healthyfoods']
    products = db.products
    list = ["en:meals", "en:meats","en:seafood","en:dairies","en:cheeses", "fr:salade-de-poulet-curry", "en:soupe","en:seafood","en:fishes"]
    return products.find({"categories_tags": { "$in": list }})

def getSnacksCandies(uri):
    client = MongoClient(uri)
    db = client['healthyfoods']
    products = db.products
    list = ["en:desserts","en:salty-snacks", "en:waffles", "en:sugary-snacks", "en:chocolates"]
    return products.find({"categories_tags": { "$in": list }})

def getLastUser(uri):
    client = MongoClient(uri)
    db = client['healthyfoods']
    users = db.users
    print "==== User Acquired ===="
    return users.find().sort("_id",1).limit(1)

def getProductsWithID(uri, list):
    client = MongoClient(uri)
    db = client['healthyfoods']
    products = db.products
    print "==== Fav Products Acquired ===="
    return products.find({"_id": {"$in": list}})

# Discover things, explore similar products... not related to user profile.
def similar_products(uri, products,name):
    client = MongoClient(uri)
    db = client['healthyfoods']
    output = []
    for a in products:
        score = 0.0
        key_a = a["_keywords"]
        table = []
        for b in products:
            key_b   = b["_keywords"]
            nutri   = "";
            key_max = max(len(key_a), len(key_b))
            key_a = key_a + [0]*(key_max - len(key_a))
            key_b = key_b + [0]*(key_max - len(key_b))
            score = jaccard_similarity_score(key_a, key_b)
            if "nutrition_grade_fr" in b:
                nutri = b["nutrition_grade_fr"]
            if(score < 1.0 and score > 0.5): # and > 0.5 to get the most similar products.
                table.append({"pid": b["_id"], "score": score, "healthy": nutri})# "product": b})
        output.append({"pid": a["_id"], "similarity" : table, "name": name})
    #pprint.pprint(output)
    result = db.similar.insert_many(output)
    print "done... "
    return 0;

def similarity_test(a,b):
    return jaccard_similarity_score(a,b)

# Based in the products the user usually likes, find healthy alternatives.
def alternative_products(uri, favorites, products):
    client = MongoClient(uri)
    db = client['healthyfoods']
    output = []
    for a in products:
        score = 0.0
        key_a = a["_keywords"]
        table = []
        for b in favorites:
            key_b   = b["_keywords"]
            key_max = max(len(key_a), len(key_b))
            key_a = key_a + [0]*(key_max - len(key_a))
            key_b = key_b + [0]*(key_max - len(key_b))
            score = jaccard_similarity_score(key_a, key_b)
            if(score < 1.0 and score > 0.5): # and > 0.5 to get the most similar products.
                table.append({"_id": b["_id"], "score": score})# "product": b})
        output.append({"_id": a["_id"], "similarity" : table})
    result = db.alternative.insert_many(output)
    return 0;

def deleteAllSimilar(uri,name):
    client = MongoClient(uri)
    db = client['healthyfoods']
    result = db.similar.delete_many({"name":name})
    return result.deleted_count

def deleteAllAlternative(uri):
    client = MongoClient(uri)
    db = client['healthyfoods']
    result = db.alternative.delete_many({})
    return result.deleted_count


def scrapSimilars(uri):
    client = MongoClient(uri)
    db = client['healthyfoods']
    similar = db.similar.find()
    with open('names.csv', 'w') as csvfile:
        fieldnames = ['pid', 'similar']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for a in similar:
            pid = a["pid"]
            table = []
            sorted_list = a["similarity"] #.sort(key = lambda x: x.score)
            print sorted_list
            for b in sorted_list:
                table.append(b["pid"])
            writer.writerow({'pid': pid, 'similar': table})

    #pprint.pprint(output)
    return 0;
