import requests
import datetime as df

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "saDIUH3254153SADxzxSADwrsa"
USERNAME = "isaactctd"
GRAPH_ID = "graph1"


user_params = {

    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_config = {
    "date": str(df.datetime.now().strftime("%Y%m%d")),
    "quantity": "0.1"
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

pixel_config1 = {
    "quantity": "0.05"
}

# response = requests.put(f"{pixel_endpoint}/20230408", json=pixel_config1, headers=headers)
# print(response.text)

response = requests.delete(f"{pixel_endpoint}/20230408", headers=headers)
print(response.text)
