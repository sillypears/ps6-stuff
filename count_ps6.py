import json

with open('ps6.json', 'r') as f:
  data = json.load(f)

count = {}

for x in data:
  if x['day'] in count.keys():
    count[x['day']] += x['quantity']
  else:
    count[x['day']] = x['quantity']

total = 0
for price in count.keys():
    print(f"Day{price}: {count[price]}")
    total += count[price]
print(f"Total (over {len(count)} days): {total}")