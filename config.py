import pymongo
import certifi

con_str = "mongodb+srv://vonellisabrea:Airforce1@cluster0.ihvtj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("soleshopstore")