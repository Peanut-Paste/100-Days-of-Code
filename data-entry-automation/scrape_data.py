import requests
from bs4 import BeautifulSoup

url = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.63417331103516%2C%22east%22%3A-122.23248568896484%2C%22south%22%3A37.662044543503555%2C%22north%22%3A37.88836615784793%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A604441%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                  "112.0.0.0 Safari/537.36"
                  "(KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/"
              "*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "sec-ch-ua": '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "x-forwarded-proto": "https",
    "x-https": "on",
    "X-Forwarded-For": "115.66.79.151",

}


class ScapeData(BeautifulSoup):
    def __init__(self):
        super().__init__(self.get_html(), "html.parser")
        self.price = []
        self.address = []
        self.link = []
        self.get_data()

    def get_html(self):
        return requests.get(url=url, headers=headers).text

    def get_data(self):
        self.price = [i.getText().split("+")[0] for i in self.find_all("span", {"data-test": "property-card-price"})]
        self.address = [i.getText() for i in self.find_all("address", {"data-test": "property-card-addr"})]
        for i in self.find_all("a", {"data-test": "property-card-link", "tabindex": "0"}):
            if i.get("href")[0] == "/":
                self.link.append(f"https://www.zillow.com{i.get('href')}")
            else:
                self.link.append(i.get('href'))
