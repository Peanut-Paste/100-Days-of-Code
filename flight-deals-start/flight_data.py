class FlightData:
    def __init__(self,price, departure_n, departure_code, arrival_n, arrival_code,
                 outbound_date, inbound_date):
        self.price = price
        self.departure_n = departure_n
        self.departure_code = departure_code
        self.arrival_n = arrival_n
        self.arrival_code = arrival_code
        self.outbound_date = outbound_date
        self.inbound_date = inbound_date
