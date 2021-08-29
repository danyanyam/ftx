from urllib.parse import urlencode
import json
import requests
import json
import hashlib
import hmac
import time

servertime = requests.get("https://api.binance.com/api/v1/time")
servertimeobject = json.loads(servertime.text)
servertimeint = servertimeobject['serverTime']

params = urlencode({
    "signature" : hashedsig,
    "timestamp" : servertimeint,
    "type" : "SPOT"
})
headers = {
    "X-MBX-APIKEY" : apikey,
}

hashedsig = hmac.new(secret.encode(), params.encode(), hashlib.sha256).hexdigest()