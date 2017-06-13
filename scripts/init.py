# -*- coding: UTF-8 -*-
import pprint
import rsystem
import keys

products = list(rsystem.getProducts(keys.URI))
drinks   = list(rsystem.getDrinks(keys.URI))
veggies  = list(rsystem.getVeggiesFruits(keys.URI))
proteins = list(rsystem.getProteins(keys.URI))
snacks   = list(rsystem.getSnacksCandies(keys.URI))

#favorites = list(rsystem.getLastUser(keys.URI))[0]["favorites"]
#p_fav     = list(rsystem.getProductsWithID(keys.URI, favorites))
# rsystem.deleteAllAlternative(keys.URI)
# rsystem.alternative_products(keys.URI, p_fav, products)

# rsystem.deleteAllSimilar(keys.URI,"drinks")
# rsystem.deleteAllSimilar(keys.URI,"veggies")
# rsystem.deleteAllSimilar(keys.URI,"proteins")
# rsystem.deleteAllSimilar(keys.URI,"snacks")
# rsystem.deleteAllSimilar(keys.URI,"all")
#
# rsystem.similar_products(keys.URI, drinks,   "drinks")
# rsystem.similar_products(keys.URI, veggies,  "veggies")
# rsystem.similar_products(keys.URI, proteins, "proteins")
# rsystem.similar_products(keys.URI, snacks,   "snacks")
# rsystem.similar_products(keys.URI, products,   "all")

rsystem.scrapSimilars(keys.URI)

# a = ["a"]
# b = ["a", "b", "c"]
# print rsystem.similarity_test(a,b)
