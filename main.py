import mongo_connection

conn = mongo_connection.connect()
 
#print(conn.list_database_names())
db = conn["python_data_DB"]
#tulostetan kaikki db collections
print(db.list_collection_names())
