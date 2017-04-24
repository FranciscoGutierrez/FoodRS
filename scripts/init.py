# -*- coding: UTF-8 -*-
import json
import rsystem
import pprint
import keys
import numpy as np
from sklearn.metrics import jaccard_similarity_score

# a = ["alpha", "bravo", "charlie", "tom"]
# b = ["alpha", "bravo", "charlie", "tom"]
#print jaccard_similarity_score(a, b)
products = list(rsystem.getProducts(keys.URI))
# pprint.pprint(products)

output = []
for a in products:
    table = []
    for b in products:
        score = jaccard_similarity_score(a["tags"], b["tags"])
        table.append({"_id": b["_id"], "score": score, "product": b})
    output.append({"_id": a["_id"], "similarity" : table})

pprint.pprint(output)
