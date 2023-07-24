from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.python.org/")
# price = driver.find_element(By.XPATH, "span[@class='a-price-whole']")
# print(price.text)

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_date = [time.text for time in driver.find_elements(By.CSS_SELECTOR, ".event-widget time")]

event_name = [name.text for name in driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")]


event_dict = {
    i: {"time:": event_date[i], "name": event_name[i]} for i in range(len(event_date))
}

print(event_dict)

driver.quit()

