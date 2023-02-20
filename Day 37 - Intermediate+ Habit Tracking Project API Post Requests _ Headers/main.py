import requests
import datetime

USERNAME = "ttishere"
TOKEN = "williamandsamuel"
GRAPH_ID = "graph1"
date = datetime.date.today()
todays_date = date.strftime("%Y%m%d")


# creating a user account with pixela
pixela_user_endpoint = "https://pixe.la/v1/users"
user_param = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_user_endpoint, json=user_param)
# print(response.text)

# creating graph with pixela
graph_endpoint = f"{pixela_user_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding",
    "unit": "commit",
    "type": "int",
    "color": "kuro",
}

headers = {"X-USER-TOKEN": TOKEN}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# posting value to pixela
post_value_endpoint = f"{pixela_user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
post_value_config = {
    "date": todays_date,
    "quantity": input("How many commits did you make today?: "),
}

response = requests.post(
    url=post_value_endpoint, json=post_value_config, headers=headers
)
print(response.text)

# Update a pixel
update_endpoint = f"{pixela_user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230219"
update_config = {
    "quantity": "1",
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

# delete a pixel
delete_endpoint = f"{pixela_user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{todays_date}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
