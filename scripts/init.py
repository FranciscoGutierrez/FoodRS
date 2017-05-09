# -*- coding: UTF-8 -*-
import pprint
import rsystem
import keys

products  = list(rsystem.getProducts(keys.URI))
favorites = list(rsystem.getLastUser(keys.URI))[0]["favorites"]
p_fav     = list(rsystem.getProductsWithID(keys.URI, favorites))

rsystem.deleteAllAlternative(keys.URI)
rsystem.alternative_products(keys.URI, p_fav, products)

rsystem.deleteAllSimilar(keys.URI)
rsystem.similar_products(keys.URI, products)


# a = ["a"]
# b = ["a", "b", "c"]
# print rsystem.similarity_test(a,b)
