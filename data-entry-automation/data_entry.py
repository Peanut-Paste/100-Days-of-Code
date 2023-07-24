from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataEntry:
    def __init__(self, driver, link):
        self.driver = driver
        self.driver.get(link)

    def input_data(self, addr, price, link):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-describedby="i2 i3"]'))
        )
        self.driver.find_element(By.CSS_SELECTOR, 'input[aria-describedby="i2 i3"]').send_keys(addr)
        self.driver.find_element(By.CSS_SELECTOR, 'input[aria-describedby="i6 i7"]').send_keys(price)
        self.driver.find_element(By.CSS_SELECTOR, 'input[aria-describedby="i10 i11"]').send_keys(link)
        self.driver.find_element(By.CSS_SELECTOR, 'div[role="button"] span.NPEfkd').click()
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Submit another response"))
        )
        self.driver.find_element(By.LINK_TEXT, "Submit another response").click()
