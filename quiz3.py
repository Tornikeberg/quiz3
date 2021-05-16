import requests
import json
import sqlite3
url = "https://api.coinlore.net/api/tickers/"

r = requests.get(url)
# print(r.status_code)
# print(r.headers)
# print(r.text)



r2 = r.json()

# with open('bitcoin.json','w') as bitcoin:
#     json.dump(r2,bitcoin,indent=4)
#


# for e in r2['data']:
#     print(e["name"]+', '+e["price_usd"])



c = sqlite3.connect('aligarx.sqlite')
cursor = c.cursor()



cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50),
                price_usd VARCHAR(255),
                rank INTEGER)
''')


cxrili = []
for b in r2['data']:
    name = b['name']
    price = b['price_usd']
    rank = b['rank']
    cxrili2 = [name,price,rank]
    cxrili.append(cxrili2)


cursor.executemany('''INSERT INTO bitcoin (name,price_usd,rank)
                      VALUES (?,?,?)''',cxrili)



c.commit()
c.close()