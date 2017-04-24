# -*- coding: UTF-8 -*-
import json
import rsystem
import pprint
import keys

products = list(rsystem.getProducts(keys.URI))
rsystem.deleteAllSimilar()
rsystem.deleteAllAlternative()
rsystem.similar_products(keys.URI, products)
