# FoodRS
A basic recommender system based on similarity of products.

# Documentation

## Restore Open Food Facts db
``
mongorestore -h localhost:27017 -d products dump/off/
``

## Test if there are records...
``
db.products.find({"countries":{ $regex : /^Be/ }}).count()
``
## Export only Belgian Products:
``
mongodump --db products --collection products --query '{"countries":{ $regex : /^Be/ }}'
``

## Drop products
``
db.products.drop()
``

## Restore Belgian screenshot dump:
``
mongorestore -h localhost:27017 -d products dump/products/
``


## MLab queries
``
mongorestore -h ds161400.mlab.com:61400 -d healthyfoods -c products -u <username> -p <password> dump/products/
``
