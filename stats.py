import json

f = open("dataset.txt", "r")

print(f.read())

# Initialize JSON data
json_data = json.loads(str(f))

  
# Create Python object from JSON string data
obj = json.loads(json_data)
  
# Pretty Print JSON
json_formatted_str = json.dumps(obj, indent=4)
print(json_formatted_str)

f.close()