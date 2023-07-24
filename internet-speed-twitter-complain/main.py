from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import internet_speed_twitter_bot

TWITTER_EMAIL = "isaac.ctd@gmail.com"
TWITTER_PASSWORD = "lCTr(6vG0p4n#*y1"
USERNAME = "@PeanutPasteS"


bot = internet_speed_twitter_bot.InternetSpeedTwitterBot()
options = ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.speedtest.net/")
bot.get_internet_speed(driver)
bot.twitter_complain(driver, TWITTER_EMAIL, TWITTER_PASSWORD, USERNAME)
