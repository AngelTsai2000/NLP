import json

with open('./vocabulary_7.json') as f:
    data = json.load(f)
with open("./result/vocabulary_7.json", "w", encoding = 'utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii = False, indent = 2)