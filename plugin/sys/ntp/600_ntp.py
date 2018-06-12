#!-*- coding:utf8 -*-

import requests
import time
import json

ts = int(time.time())
payload = [
    {
        "endpoint": "siplug",
        "metric": "plugtest",
        "timestamp": ts,
        "step": 60,
        "value": 0.123,
        "counterType": "GAUGE",
        "tags": "idc=lg,loc=beijing",
    },
]

r = requests.post("http://192.168.115.49:1988/v1/push", data=json.dumps(payload))
print r.text
