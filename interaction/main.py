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

driver.get("https://www.adidas.com.sg/men")

# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# article_count.click()

# view_source = driver.find_element(By.LINK_TEXT, "View source")
# view_source.click()

search = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div/div/d'
                                            'iv[1]/div/header/div[2]/div/div[2]/div/input')
search.send_keys("nmd")
search.send_keys(Keys.ENTER)
time.sleep(1)

cross = driver.find_element(By.CSS_SELECTOR, ".gl-modal--mobile-full .gl-modal__close")
cross.click()

first = driver.find_element(By.CSS_SELECTOR, ".glass-product-card__assets a")
first.click()

