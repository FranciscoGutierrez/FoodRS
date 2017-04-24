# -*- coding: UTF-8 -*-
import rsystem
import keys

products = list(rsystem.getProducts(keys.URI))
rsystem.deleteAllSimilar()
rsystem.deleteAllAlternative()
rsystem.similar_products(keys.URI, products)
