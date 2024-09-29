import requests

# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# print(response.json())

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

parameters = {
    'lat': 6.944139,
    'lng': 122.075540,
    'formatted': 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)

response.raise_for_status()
data = response.json()

print(data)

sunrise = str(str(data["results"]["sunrise"]).split("T")[1]).split("+")[0]
sunset =  str(str(data["results"]["sunset"]).split("T")[1]).split("+")[0]
print(f"{sunrise, sunset}")