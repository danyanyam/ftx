from urllib.parse import urlencode
import json
import requests
import json
import hashlib
import hmac
import time
from config import api_key, secret_key
from pprint import pprint

endpoint = "/sapi/v1/capital/config/getall"

servertime = requests.get("https://api.binance.com/api/v1/time")
servertimeobject = json.loads(servertime.text)
servertimeint = servertimeobject['serverTime']

params = urlencode({
    "timestamp": servertimeint
})

signature = hmac.new(secret_key.encode(), params.encode(), hashlib.sha256).hexdigest()

params = {
    "timestamp": servertimeint,
    "signature": signature
}

headers = {
    "X-MBX-APIKEY": api_key
}

r = requests.get('https://api.binance.com' + endpoint, headers=headers, params=params)
response = json.loads(r.text)
print(json.dumps(response, indent=4, sort_keys=True))
