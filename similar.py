import tfidf
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
    client = MongoClient('mongodb://localhost:27017/')
