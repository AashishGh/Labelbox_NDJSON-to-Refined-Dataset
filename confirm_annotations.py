import json

with open('annotations.ndjson', 'r') as f:
    lines = f.readlines()

record = json.loads(lines[0])
print(json.dumps(record, indent=2))
