from tfidf import tfidf
import mduri
import pprint
from pymongo import MongoClient

def jaccard_index(set1, set2):
    n = len(set1.intersection(set2))
    return n / float(len(set1) + len(set2) - n)

def tfidf():
    table = tfidf.tfidf()
    table.addDocument("foo", ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel"])
    table.addDocument("bar", ["alpha", "bravo", "charlie", "india", "juliet", "kilo"])
    table.addDocument("baz", ["kilo", "lima", "mike", "november"])
    return table.similarities (["alpha", "bravo", "charlie"]) # => [['foo', 0.6875], ['bar', 0.75], ['baz', 0.0]]

def mongodb():
    # Mongo URI: "mongodb://<user>:<password>@ds161400.mlab.com:61400/healthyfoods"
    client = MongoClient(mduri.MURI)
    db = client['healthyfoods']
    #collection = db['products']
    products = db.products
    pprint.pprint(products.find_one())

# Discover things, explore similar products... not related to user profile.
def similar_products():
    mongodb()
    # Scan all the tags of the products.
    # Calculate similarity between all the products using the tags.
    # Keep the top 10 similar products.
    # Create a <similar> collection of products (Just Store name and ID).
    # end.

# Based in the products I usually like, find healthy alternatives.
def alternative_products():
    mongodb()
    # Get the last user in the session.
    # Calculate tfidf between all products between user profile and products collection.
    # Mix nutriscore and similarityscore to *bump* healthier products.
    # Keep the top 10 similar products.
    # Create a <alternatives> collection of products. (Just store name and ID).
    # end.
