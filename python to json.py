import json
x = {                        #python dictionary
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)     #converting to json file
print(y)