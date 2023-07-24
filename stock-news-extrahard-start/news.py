import requests

NEWS_API = "29f1b73466344c6592f7422c348a0c63"


class News:
    def __init__(self, company_name):
        self.search = company_name
        self.latest_news = []
        self.get_news()

    def get_news(self):
        news_parameter = {
            "apiKey": NEWS_API,
            "q": self.search,
            "sortBy": "publishedAt",
            "pageSize": 10
        }
        response = requests.get("https://newsapi.org/v2/everything", params=news_parameter)
        news_list = response.json()["articles"][:3]
        self.latest_news = [[i["title"], i["description"], i["url"]] for i in news_list]


