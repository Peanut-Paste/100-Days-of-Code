from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time


def scroll_container_to_bottom(driver, container_element, timeout=1, scroll_step=200):
    prev_scroll_top = 0
    new_scroll_top = scroll_step

    while prev_scroll_top < new_scroll_top:
        driver.execute_script("arguments[0].scrollTo(0, arguments[1]);", container_element, new_scroll_top)
        time.sleep(timeout)

        prev_scroll_top = new_scroll_top
        new_scroll_top += scroll_step
        max_scroll_top = driver.execute_script("return arguments[0].scrollHeight - arguments[0].clientHeight;", container_element)

        if new_scroll_top > max_scroll_top:
            new_scroll_top = max_scroll_top


options = ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3533318344&f_LF=f_AL&geoId=102454443&keywords"
           "=python%20developer&location=Singapore&refresh=true")


sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

user_name = driver.find_element(By.ID, "username")
user_name.send_keys("tanjingyi1997@hotmail.com")
pass_word = driver.find_element(By.ID, "password")
pass_word.send_keys("Tanjingyi1997")
pass_word.send_keys(Keys.ENTER)

time.sleep(3)
container_element = driver.find_element(By.CSS_SELECTOR, ".jobs-search-results-list")
scroll_container_to_bottom(driver=driver, container_element=container_element)

job_container = driver.find_elements(
    By.CSS_SELECTOR,
    ".scaffold-layout__list-container"
    " li",
)

joblinks = []

for jobs in job_container:
    try:
        anchor = jobs.find_element(By.CSS_SELECTOR, "a")
        joblinks.append(anchor)
    except NoSuchElementException:
        pass

links = [link.get_attribute("href") for link in joblinks]

for link in links:
    driver.get(link)
    time.sleep(5)





