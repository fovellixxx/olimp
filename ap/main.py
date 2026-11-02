import os
import requests

api_token = 'k7eBpORoO7clwUfckXe4zCH1DrU_7eozNfBiqgGCAgw'
low=1
high=1024

while True: 
    power = (low + high) // 2
    response = requests.post(
        "https://artillery.apps.botops.ru/api/fire",
        json={"player": "student", "power": power},
        headers={"X-Game-Session": api_token},
        timeout=10,
    )
    response.raise_for_status()
    log=response.json()

    if log.get('result') == 'undershoot':
        low = power + 1
    if log.get('result') == 'overshoot':
        high = power - 1
    print(log)
