import json

#LOADS
json_string = '{"name": "Donald Duck, "isCartoon":true}'
d = json.loads(json_string)
print(type(d))
print(d)


#LOAD mavatan json tyyppinen 
with open('aku.json', 'r', encoding="utf-8") as file:
    aku_dict = json.load(file)
    print(type(aku_dict))
    print(aku_dict)