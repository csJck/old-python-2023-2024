import requests as rq
import sys
import json

response = rq.get("https://api.coindesk.com/v1/bpi/currentprice.json")
object = response.json()
rate = object['bpi']['USD']['rate']

try:
    amount = float(sys.argv[1])

except ValueError:
    sys.exit()

else:
    if len(sys.argv) > 2:
        sys.exit()


price = float(rate.replace(',', '')) 
cost = price * amount


print(f"${cost:,.2f}")
    
