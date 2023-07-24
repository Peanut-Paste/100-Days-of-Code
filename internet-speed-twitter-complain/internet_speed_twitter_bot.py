from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 1000
PROMISED_UP = 1000


class InternetSpeedTwitterBot:
    def __init__(self):
        self.download = 0
        self.upload = 0
        self.complain_text = ""

    def get_internet_speed(self, driver):
        start = driver.find_element(By.CSS_SELECTOR, ".start-text")
        start.click()
        time.sleep(47)
        self.download = float(driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.upload = float(driver.find_element(By.CLASS_NAME, "upload-speed").text)

    def twitter_complain(self, driver, email, password, username):
        if self.download < PROMISED_DOWN or self.upload < PROMISED_UP:
            self.complain_text = f"Hey Internet Provider, why is my internet speed {self.download} down / " \
                                 f"{self.upload} up. when I pay for {PROMISED_DOWN} down / {PROMISED_UP} up?"
            driver.get("https://www.twitter.com")
            time.sleep(3)
            driver.find_element(By.LINK_TEXT, "Log in").click()
            time.sleep(3)
            driver.find_element(By.CSS_SELECTOR, "div.css-1dbjc4n").click()
            time.sleep(1)
            email_input = driver.find_element(By.CSS_SELECTOR, "input.r-30o5oe")
            email_input.send_keys(email)
            email_input.send_keys(Keys.ENTER)
            time.sleep(2)

            username_input = driver.find_element(By.CSS_SELECTOR, "input.r-30o5oe")
            username_input.send_keys(username)
            username_input.send_keys(Keys.ENTER)

            time.sleep(2)
            password_input = driver.find_element(By.NAME, "password")
            password_input.send_keys(password)
            password_input.send_keys(Keys.ENTER)

            time.sleep(3)
            try:
                driver.find_element(By.CSS_SELECTOR, "svg.r-4qtqp9").click()
            except NoSuchElementException:
                pass

            driver.find_element(By.CSS_SELECTOR, "div.css-1dbjc4n").click()
            textbox = driver.find_element(By.CSS_SELECTOR, "div.public-DraftStyleDefault-block")
            textbox.send_keys(self.complain_text)
            time.sleep(2)
            driver.find_element(By.XPATH,
                                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()

        else:
            print("Everything checks out")