import env_data
import requests
from flight_search import FlightSearch
from data_manager import DataManager

def get_data():
    response = requests.get(f"https://api.sheety.co/{env_data.SHEETY_USERNAME}/{env_data.SHEETY_PROJECT_NAME}/{env_data.SHEETY_SHEET_NAME}", headers = {"Authorization": f"Bearer {env_data.SHEETY_BEARER_TOKEN}"})
    response.raise_for_status()

    return response.json()

sheet_data = get_data()
i = 0
for city in sheet_data["prices"]:
    if city["iataCode"] == "":
        IATA = FlightSearch(city_name = city["city"]).get_IATA()
        sheet_data["prices"][i]["iataCode"] = IATA["IATA"]
        sheet_data["prices"][i]["skyId"] = IATA["skyId"]
    i += 1
    
print (sheet_data)

dm = DataManager(sheet_data = sheet_data)
dm.update_google_sheet()