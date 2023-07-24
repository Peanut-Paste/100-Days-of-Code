import requests

SHEETY_URL = "https://api.sheety.co/b9ee8ce6bdb18e42b20524d1e8093966/flightDeals/"


class DataManager:
    def __init__(self, sheet):
        self.response = requests.get(SHEETY_URL + sheet)
        self.data = self.response.json()[sheet]

    def edit_row(self, column, row_id, data):
            edit_params = {
                "price": {
                    column: data
                }
            }
            requests.put(f"https://api.sheety.co/b9ee8ce6bdb18e42b20524d1e8093966/flightDeals/prices/{row_id}",
                         json=edit_params)

    def add_row(self, first_n, last_n, email):
        add_params = {
            "user": {
                "firstName": first_n,
                "lastName": last_n,
                "email": email,
            }
        }
        requests.post("https://api.sheety.co/b9ee8ce6bdb18e42b20524d1e8093966/flightDeals/users",
                     json=add_params)