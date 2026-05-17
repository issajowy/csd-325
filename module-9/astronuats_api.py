import requests

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print("Number of people in space:", data["number"])
    for person in data["people"]:
        print("-", person["name"])
else:
    print("Failed to retrieve data.")