
import requests

question_count = input("How many questions would you like to have? ")

if str(question_count).isdigit():
    response = requests.get("https://opentdb.com/api.php", params = {"amount": int(question_count), "type": "boolean"})
    response.raise_for_status()

    response_data = response.json()

    question_data = response_data["results"]
else:
    quit()
