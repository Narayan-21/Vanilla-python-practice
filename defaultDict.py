from collections import defaultdict
import random
from collections import Counter

# Application of defaultdict => When we are building up a dict and we would like to avoid write 'if key in dict - else'

#1
d={}
random.seed(0)
data = [random.randint(1,5) for i in range(10000)]

for number in data:
    if number in d:
        d[number] += 1
    else:
        d[number] = 1

print(d)

#2
dd = defaultdict(lambda: 0)
for number in data:
    dd[number] += 1

print(dd)


#3
print(Counter(data))

#4
from uuid import uuid4
random.seed(0)
suppliers= ['aaa','bbb','ccc','ddd','eee']
clients = ['zzz', 'yyy', 'xxx', 'www']
orders = [
    {
        'suppliers': random.choice(suppliers),
        'clients': random.choice(clients),
        'order_no': str(uuid4()),
        'item_id': str(uuid4()),
        'quantity': random.randint(1,100)
    }
    for i in range(100)
]

client_orders={}
for order in orders:
    client = order['clients']
    if client in client_orders:
        client_orders[client].append(order)
    else:
        client_orders[client] = [order]

print(client_orders)

#5
client_orders_dd = defaultdict(list)
for order in orders:
    client = order['clients']
    client_orders_dd[client].append(order)
print(client_orders_dd)