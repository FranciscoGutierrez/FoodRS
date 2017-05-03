# -*- coding: UTF-8 -*-
import pprint
import rsystem
import keys

products = list(rsystem.getProducts(keys.URI))
rsystem.deleteAllSimilar(keys.URI)
rsystem.deleteAllAlternative(keys.URI)
rsystem.similar_products(keys.URI, products)


# a = ["a"]
# b = ["a", "b", "c"]
# print rsystem.similarity_test(a,b)
