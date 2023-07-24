import requests

STOCK_API = "I3VEQU427KFICJM6"

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price_diff_p = 0
        self.get_stock_data()

    def get_stock_data(self):
        stock_parameter = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": self.symbol,
            "outputsize": "compact",
            "apikey": STOCK_API,
        }
        response = requests.get("https://www.alphavantage.co/query", params=stock_parameter)
        stock_data = response.json()["Time Series (Daily)"]
        stock_list = [value for (key, value) in stock_data.items()]
        yesterday_price = float(stock_list[0]["4. close"])
        day_before_price = float(stock_list[1]["4. close"])
        self.price_diff_p = (yesterday_price - day_before_price) / yesterday_price

    def check_is_per(self):
        if self.price_diff_p >= 0.05 or self.price_diff_p <= -0.05:
            return True


