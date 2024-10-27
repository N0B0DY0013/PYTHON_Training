
import requests
import os
import dotenv
from datetime import datetime

dotenv.load_dotenv()

NUTRIONIX_APP_ID = os.getenv("NUTRIONIX_APP_ID")
NUTRIONIX_APPLICATION_KEY = os.getenv("NUTRIONIX_APPLICATION_KEY")

excercise_text = input("Tell me which exercise you did:\n")

if excercise_text != "" and excercise_text != None:

    response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", json = {"query": excercise_text},
                                                                                     headers = {"x-app-id": NUTRIONIX_APP_ID,
                                                                                                "x-app-key": NUTRIONIX_APPLICATION_KEY})
    response.raise_for_status()

    data = response.json()
    
    SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
    SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")
    SHEETY_PROJECT_NAME = "20241027MyWorkOut"
    SHEETY_SHEET_NAME = "workouts"
    
    for exercise in data["exercises"]:
        response = requests.post(f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET_NAME}", json = {"workout": {"date": datetime.today().strftime("%Y-%m-%d"),
                                                                                                                                                   "time": datetime.today().strftime("%H:%M:%S"),
                                                                                                                                                   "exercise": exercise["name"],
                                                                                                                                                   "duration": exercise["duration_min"],
                                                                                                                                                   "calories": exercise["nf_calories"]}},
                                                                                                                        headers = {"Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"})
        response.raise_for_status()
        
        print(response.json())
        
        
        
    
    