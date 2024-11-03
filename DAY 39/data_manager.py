import env_data
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self, sheet_data) -> None:
        self.sheet_data = sheet_data
        
    def update_google_sheet(self):
        for city in self.sheet_data["prices"]:
            response = requests.put(f"https://api.sheety.co/{env_data.SHEETY_USERNAME}/{env_data.SHEETY_PROJECT_NAME}/{env_data.SHEETY_SHEET_NAME}/{city['id']}", headers = {"Authorization": f"Bearer {env_data.SHEETY_BEARER_TOKEN}"}, json = {"price": {"iataCode": city["iataCode"],
                                                                                                                                                                                                                                                           "skyId": city["skyId"]}})
