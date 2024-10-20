import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

PIXELA_USER_TOKEN = os.getenv("PIXELA_USER_TOKEN")
PIXELA_USER_NAME = os.getenv("PIXELA_USER_NAME")

# CREATE USER ...
PIXELA_END_POINT = "https://pixe.la/v1/users"
url_params = {
    "token": PIXELA_USER_TOKEN,
    "username": PIXELA_USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url = PIXELA_END_POINT, json = url_params)
# print(response.text)

url_params = {}

# CREATE GRAPH ...
PIXELA_CREATE_GRAPH_END_POINT = f"https://pixe.la/v1/users/{PIXELA_USER_NAME}/graphs"
PIXELA_GRAPH_ID = "graph1"
url_params = {
    "id": PIXELA_GRAPH_ID,
    "name": "Graph 1",
    "unit": "commit",
    "type": "float",
    "color": "shibafu",
    "timezone": "Asia/Manila",
 }

# response = requests.post(url = PIXELA_CREATE_GRAPH_END_POINT, json = url_params, headers = {"X-USER-TOKEN": PIXELA_USER_TOKEN})
# print(response.text)

url_params = {}

# POST VALUE TO THE GRAPH ...
PIXELA_POST_GRAPH_END_POINT = f"https://pixe.la/v1/users/{PIXELA_USER_NAME}/graphs/{PIXELA_GRAPH_ID}"
url_params = {
    "date": datetime.today().strftime("%Y%m%d"),
    "quantity": "13",
    "optionalData": '{"comment": "This is a sample posting..."}'
}

response = requests.post(url = PIXELA_POST_GRAPH_END_POINT, json = url_params, headers = {"X-USER-TOKEN": PIXELA_USER_TOKEN})
print(response.text)

url_params = {}

# UPDATE A PIXEL ...
PIXELA_UPDATE_PIXEL_END_POINT = f"https://pixe.la/v1/users/{PIXELA_USER_NAME}/graphs/{PIXELA_GRAPH_ID}/{datetime.today().strftime('%Y%m%d')}"
url_params = {
    "quantity": "1"
}
response = requests.put(url = PIXELA_UPDATE_PIXEL_END_POINT, json = url_params, headers = {"X-USER-TOKEN": PIXELA_USER_TOKEN})
print(response.text)

# DELETE A PIXEL ...
PIXELA_DELETE_PIXEL_END_POINT = f"https://pixe.la/v1/users/{PIXELA_USER_NAME}/graphs/{PIXELA_GRAPH_ID}/{datetime.today().strftime('%Y%m%d')}"
response = requests.delete(url = PIXELA_DELETE_PIXEL_END_POINT, headers = {"X-USER-TOKEN": PIXELA_USER_TOKEN})
print(response.text)