import os
import pymongo


if os.path.exists("env.py"):
    import env


    MONGO_URI = "mongodb+srv://Sebastian:Gabbeluba@ms3cluster.qruwl.mongodb.net/ms3_seriesdb?retryWrites=true&w=majority"
    DATABASE = "ms3_seriesdb"
    COLLECTION = "series"


    def mongo_connect(url):
        try:
            conn = pymongo.MongoClient(url)
            print("Mongo is connected")
            return conn
        except pymongo.errors.ConnectionFailure as e:
            print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

documents = coll.find()

for doc in documents:
    print(doc)
