#!-*- coding:utf8 -*-

import requests
import time
import json

for  xx in range(1,100):
    ts = int(time.time())
    payload = [
        {
            "endpoint": "test-endpoint",
            "metric": "plugtest",
            "timestamp": ts,
            "step": 30,
            "value": xx,
            "counterType": "GAUGE",
            "tags": "idc=lg,loc=beijing",
        },
    ]

    r = requests.post("http://192.168.115.49:1988/v1/push", data=json.dumps(payload))
    print "times : ",xx," : ",r.text
    time.sleep(30)

