import json

with open('ps6.json', 'r') as f:
  data = json.load(f)

prices = {}

for x in data:
  if x['day'] in prices.keys():
    prices[x['day']] += x['price']*x['quantity']
  else:
    prices[x['day']] = x['price']*x['quantity']

total = 0
for price in prices.keys():
    print(f"Day{price}: ${prices[price]}")
    total += prices[price]
print(f"Total (over {len(prices)} days): ${total}")