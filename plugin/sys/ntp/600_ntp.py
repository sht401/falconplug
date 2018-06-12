
import time
import json


output = [{"endpoint": "si-plug",
           "metric": "agent.plug",
           "tags": "",
           "timestamp": int(time.time()),
           "value": 1.6,
           "counterType": "GAUGE",
           "step": 60}]

print  json.dumps(output)
