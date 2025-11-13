#python to json
#dict to object 0javascript object
#tuple to array
#str to string
#str to string
#int to number
#float to number
#true to True #HUONM
#None to null #HUOM

import json

#DUMPS (dump python object to json string)
d = {#python dictionary
    "first_name": "Donald",
    "isCartoon": True,
    "age": 120,

}
#konvertoidan dictionary jsin:iksi
d_as_json = json.dumps(d, indent = 4, sort_keys=True) #separators=
print(type(d))#dictt
print(type(d_as_json))#str (json string)
print(d_as_json)

#-------------------------------------------------------------
#DUMP talennetaan json string json-tiedostoon
with open ("aku.json", "w", encoding="utf-8") as file:
    file.write(d_as_json)

    