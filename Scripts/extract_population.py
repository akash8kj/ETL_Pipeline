import requests
import json

API_KEY = "Your_Census_API_KEY"

url = f"https://api.census.gov/data/2021/pep/population?get=NAME,POP_2021&for=state:*&key={API_KEY}"

response = requests.get(url)
response.raise_for_status()

with open("data/raw/state_population.json", "w") as file:
    json.dump(response.json(), file, indent=4)

print("State population data saved successfully!")