import requests
from flight_data import FlightData

TEQUILA_URL = "https://api.tequila.kiwi.com/"

tequila_headers = {
    "apikey": "DvulD5Al54BAOPUFOud2HMgfsukfH2iy"
}

class FlightSearch:
    def get_iata_code(self, city_name):
        query_endpoint = "locations/query"
        query_params = {
                    "term": city_name,
                    "locale": "en-US",
                    "location_types": "city",
                }

        tequila_response = requests.get(TEQUILA_URL + query_endpoint, params=query_params,
                                        headers=tequila_headers)
        return tequila_response.json()["locations"][0]["code"]

    def get_flight_price(self, fly_from, code, datefrom, dateto):
        search_endpoint = "search"
        search_params = {
            "fly_from": fly_from,
            "fly_to": code,
            "date_from": datefrom.strftime("%d/%m/%Y"),
            "date_to": dateto.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 10,
            "nights_in_dst_to": 15,
            "one_for_city": 1,
            "max_stopovers": 2,
            "curr": "SGD"
        }
        response = requests.get(TEQUILA_URL+search_endpoint, params=search_params, headers=tequila_headers)

        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {code}.")
            return None
        flight_data = FlightData(
            price=data["price"],
            departure_n=data["cityFrom"],
            departure_code=data["cityCodeFrom"],
            arrival_n=data["cityTo"],
            arrival_code=data["cityCodeTo"],
            outbound_date=data["route"][0]["dTime"],
            inbound_date=data["route"][1]["dTime"]
        )
        return flight_data

