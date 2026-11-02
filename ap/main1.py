import os
import requests

api_token = '1LlGNbO5RbC_8ctG42qnX3woWl4P4fE-blfi3ksAUZo'
while True:
    response = requests.post(
        "https://artillery.apps.botops.ru/api/fire",
        json={"player": "teacher", "power": 1},
        headers={"X-Game-Session": api_token},
        timeout=10,
    )
    response.raise_for_status()
    print(response.json())