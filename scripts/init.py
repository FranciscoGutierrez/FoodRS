# -*- coding: UTF-8 -*-
import pprint
import rsystem
import keys

products = list(rsystem.getProducts(keys.URI))
drinks   = list(rsystem.getDrinks(keys.URI))
veggies  = list(rsystem.getVeggiesFruits(keys.URI))
proteins = list(rsystem.getProteins(keys.URI))
snacks   = list(rsystem.getSnacksCandies(keys.URI))

favorites = list(rsystem.getLastUser(keys.URI))[0]["favorites"]
p_fav     = list(rsystem.getProductsWithID(keys.URI, favorites))

# rsystem.deleteAllAlternative(keys.URI)
# rsystem.alternative_products(keys.URI, p_fav, products)

rsystem.deleteAllSimilar(keys.URI)
rsystem.similar_products(keys.URI, products, "similar_all")
rsystem.similar_products(keys.URI, drinks,   "similar_drinks")
rsystem.similar_products(keys.URI, veggies,  "similar_veggies")
rsystem.similar_products(keys.URI, proteins, "similar_proteins")
rsystem.similar_products(keys.URI, snacks,   "similar_snacks")



# a = ["a"]
# b = ["a", "b", "c"]
# print rsystem.similarity_test(a,b)
