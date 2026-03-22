import requests
import json

params = {"from":"USD", "to":"BRL", "amount":1}
res = requests.get("https://api.frankfurter.app/latest", params=params)

print(res.json())
