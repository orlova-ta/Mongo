class Character:
    def __init__(self, name. isCartoon,age):
        self.name = name
        self.isCartoon = isCartoon
        self.age = age


   def __repr__ (self):
    return f"Person(name={self.name}, age={self.age})"

  def __repr__(self): 
    return f"Person(name={self.name}, age={self.age})"
  def walk(self):
    print(f"{self.name} is walking")
aku = Character("Donald", True, 120)
iines = Character("Daisy", True, 25)
aku.age=150
print(aku)

import json
json_data = '{"name": "Aku", "isCartoon":true, "age":120}'
#konvertoidaan json string pythoniiksi
d = json.loads(json_string)

#luodan Charachter -luokasta olio, käytään 'dictionary unpacking'
aku = Character(**d)#using destructor to easy writing
