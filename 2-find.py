import mongo_connection
from pprint import pprint
conn = mongo_connection.connect()

#valitan tietokanta
db=conn["sample_mflix"]

#valitan db collection
coll=db["movies"]

#haetan kaikki movies data, voime palautta cursori
documents = coll.find({"genre": "Comedy"})

#lets do a loop for it
#for doc in documents:
#    pass

#for doc in documents:
 #   print(doc)


#haetan kaikki joissa vuosi on 1986
for doc in documents:
    pprint (doc)

    #uv add print

#halutan tieta montako documentia meilla on
count= coll.count_document({"genres": "Comedy"})
print(f"löytyi {count} dokumenttia")


#harjoitus hae dokumentin määrä jossa genrenä on ainakin "Comedy"