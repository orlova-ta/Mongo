from pymongo import MongoClient
#asennetan pandas
import pandas as pd
from dotenv import load_dotenv
import os


load_dotenv(override=True)
client= MongoClient(os.getenv("MONGO_URI"))
#luetaan csv tiedosto Pandasin dataframin

df= pd.read_csv("worldcities.csv")
#muutetaan Dataframe pythonin dictionaryn (convertoi dict to json)
data_dict = df.to_dict(orient="records")
#orient on oletuksena (jos sita ei aseta) dict
#muita vaihtoehtoja: list, series, spli, records
#esim.list:
#{"name":["Alice", "Bob"],
#"age":pd.Series([25,30])}

#esim.series:
#"name": pd.Series(["Alice", "Bob"], index=[0,1]),
#"age": pd.Series([25,30], index=[0,1])

#esim.records: jokaisesta rivista tule dictionary
#[
#{"name":"Alice#, "age":25}
#{"name":"Bob", "age":25}
#]

db = client["world_cities_DB"]

#coll = db["cities_collection"]
#like this can do directly contribute to db
db.cities_collection.insert_many(data_dict)

coll = db["cities_collection"]
coll = db["another_cities_collection"]


for chunk in pd.read_csv("worldcities.csv", chunksize=1000):
    coll.insert_many(chunk.to_dict(orient="records"))
