# -*- coding: UTF-8 -*-
import rsystem
import keys

products = list(rsystem.getProducts(keys.URI))
rsystem.deleteAllSimilar(keys.URI)
rsystem.deleteAllAlternative(keys.URI)
rsystem.similar_products(keys.URI, products)
