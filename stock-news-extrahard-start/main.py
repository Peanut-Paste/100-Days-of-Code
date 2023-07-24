import requests
from stock import Stock
from news import News

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


stock = Stock(STOCK)
news = News(COMPANY_NAME)
paragraph = ""

if stock.check_is_per():
    if stock.price_diff_p < 0:
        message = f"{STOCK}: 🔻{stock.price_diff_p*-100:.2f}%"
    else:
        message = f"{STOCK}: 🔺{stock.price_diff_p * 100:.2f}%"

    for new in news.latest_news:
        paragraph += f"\n\nHeadline: {new[0]}\n\nBrief: {new[1]}\n\nURL: {new[2]}"

    tele_message = message + paragraph
    parameter = {
        "chat_id": 740295348,
        "text": tele_message
    }
    url = f"https://api.telegram.org/bot6074336092:AAFUor0YoetJ4q0Nt4wyRR83-pmcg2prqZw/sendMessage"
    requests.get(url, params=parameter).json()


