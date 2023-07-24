from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime


today = datetime.now().day

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://info.bbdc.sg/visitor-appointment/")

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'table.ui-datepicker-calendar tbody tr td'))
)
datelist = [i for i in driver.find_elements(By.CSS_SELECTOR, "table.ui-datepicker-calendar tbody tr td") if i.text != " "]
curated_list = [i for i in datelist if int(i.text) > today]


for i in curated_list:
    print(i.text)