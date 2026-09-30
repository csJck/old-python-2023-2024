import requests as rq
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

response = rq.get(f"https://itunes.apple.com/search?entity=song&limit=50&term={sys.argv[1]}")

object = response.json()

x = 0

for r in object["results"]:
    x+=1
    print(x, r["trackName"])