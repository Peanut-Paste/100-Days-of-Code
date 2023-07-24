import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "Isaac.cTD@gmail.com"
MY_PASS = "dzauofhghfisuica"

product_url = "https://www.amazon.com/Zojirushi-NS-TSC10-Uncooked-Cooker-1-0-Liter/dp/B0074CDG6C/?th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/"
              "webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
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

response = requests.get(product_url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

price = float(soup.find("span", class_="a-offscreen").getText()[1:])
product_name = soup.find("span", id="productTitle").getText().strip()

if price < 140:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(from_addr= MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject: Amazon product for {product_name}\n\n"
                            f"The product dropped below your target price. It is currently at"
                            f" {price}.\n {product_url}")
