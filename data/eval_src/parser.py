import json

with open('voc-val.json') as f:
    json_data = json.load(f)
imageToid = json_data["imageToid"]
print(imageToid)