import mongo_connection
import pandas as pd
import csv #

conn = mongo_connection.connect()

#haetan kaikki collection tietueet

db=conn["world_cities_DB"]

all_records = db["cities_collection"].find()
#luodan pandas Dataframe
df =pd.DataFrame(all_records)

#poustetaan
df.pop("_id")#pop palautta arvon, eli sen voi sijoittaa muuttujan

