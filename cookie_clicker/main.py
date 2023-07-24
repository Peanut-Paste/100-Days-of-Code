from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")


stores_list = [items.text.split("-") for items in driver.find_elements(By.CSS_SELECTOR, "#store b")][0:8]
stores_dict = {
    data[0].strip(): int(data[1].strip().replace(",", "")) for data in stores_list
}

buy_this = ""
timeout = time.time() + 2
stop_program = time.time() + 60*5

while True:
    if time.time() > timeout:
        money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
        if money > stores_dict["Time machine"]:
            money -= stores_dict["Time machine"]
            buy_this = "Time machine"
            buy = driver.find_element(By.ID, f"buy{buy_this}")
            buy.click()
        if money > stores_dict["Portal"]:
            money -= stores_dict["Portal"]
            buy_this = "Portal"
            buy = driver.find_element(By.ID, f"buy{buy_this}")
            buy.click()
        if money > stores_dict["Alchemy lab"]:
            money -= stores_dict["Alchemy lab"]
            buy_this = "Alchemy lab"
            buy = driver.find_element(By.ID, f"buy{buy_this}")
            buy.click()
        if money > stores_dict["Shipment"]:
            money -= stores_dict["Shipment"]
            buy_this = "Shipment"
            buy = driver.find_element(By.ID, f"buy{buy_this}")
            buy.click()
        if money > stores_dict["Mine"]:
            money -= stores_dict["Mine"]
            buy_this = "Mine"
            buy = driver.find_element(By.ID, f"buy{buy_this}")
            buy.click()
        if money > stores_dict["Factory"]:
            money -= stores_dict["Factory"]
            buy_this = "Factory"
            buy = driver.find_element(By.ID, f"buy{buy_this}")
            buy.click()
        if money > stores_dict["Grandma"]:
            money -= stores_dict["Grandma"]
            buy_this = "Grandma"
            buy = driver.find_element(By.ID, f"buy{buy_this}")
            buy.click()
        if money > stores_dict["Cursor"]:
            money -= stores_dict["Cursor"]
            buy_this = "Cursor"
            buy = driver.find_element(By.ID, f"buy{buy_this}")
            buy.click()
        timeout = time.time() + 2

    if time.time() > stop_program:
        break
    cookie.click()

print(driver.find_element(By.ID, "cps").text)
