import json
import keys
import rsystem
import pprint

import numpy as np
from sklearn.metrics import jaccard_similarity_score


a = ["alpha", "bravo", "charlie", "tom"]
b = ["alpha", "bravo", "charlie", "tom"]
print jaccard_similarity_score(a, b)

products = list(rsystem.getProducts(keys.URI))
pprint.pprint(products)

# Add all the products to the table...
for a in products:
    for b in products:
        score = jaccard_similarity_score(a["tags"], b["tags"])
        print score


#table = tfidf.tfidf()
#table.addDocument("foo", ["alpha", "bravo", "charlie"])
#table.addDocument("bar", ["alpha", "bravo", "charlie", "india", "juliet", "kilo"])
#print table.similarities (["alpha", "bravo", "charlie"]) # => [['foo', 0.6875], ['bar', 0.75], ['baz', 0.0]]
