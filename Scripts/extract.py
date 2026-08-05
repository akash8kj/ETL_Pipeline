import requests
import json
import os

url = "https://api.openbrewerydb.org/v1/breweries"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    os.makedirs("data/raw", exist_ok=True)

    with open("data/raw/breweries.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"Success! Downloaded {len(data)} records.")
else:
    print("Error:", response.status_code)