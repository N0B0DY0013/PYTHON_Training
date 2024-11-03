import requests
import env_data

class FlightSearch:
    
    def __init__(self, city_name) -> None:
        self.city_name = city_name
        
    
    def get_IATA(self):
        

        response = requests.get("https://sky-scanner3.p.rapidapi.com/flights/auto-complete", 
                                headers = {"x-rapidapi-key": env_data.X_RAPIDAPI_KEY,
                                           "x-rapidapi-host": env_data.X_RAPIDAPI_HOST},
                                params = {"query": self.city_name,
                                          "placeTypes": "CITY,AIRPORT"})

        response.raise_for_status()
        
        result = response.json()
        
        skyId = result["data"][0]["presentation"]["skyId"]
        IATA = skyId
        if len(IATA) > 3:
            IATA = IATA[:3]
        
        return {"skyId": skyId,
                "IATA": IATA}
    
    
    #This class is responsible for talking to the Flight Search API.
    # pass
    # https://rapidapi.com/ntd119/api/sky-scanner3/playground/apiendpoint_67371907-a797-4799-bb14-873d349225c6