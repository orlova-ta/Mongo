from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv(override=True)#oletuksena False jos ei aseta
print(os.name)
mongo_uri ="mongodb+srv://Tatiana:135rt135RT@cluster0.3p7wqet.mongodb.net/?appName=Cluster0"

def connect():
    try:
       client = MongoClient(os.getenv("MONGO_URI"))
       client.admin.command("ping")
       print("Connected to Mongo")
       return client
    except :
        raise ConnectionError("Cannot connect")
#connect()    
if __name__== "__name__":
    connect()