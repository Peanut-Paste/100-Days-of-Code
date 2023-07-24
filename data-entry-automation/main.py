from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from scrape_data import ScapeData
from selenium.webdriver.chrome.options import Options
from data_entry import DataEntry

google_form_url = "https://forms.gle/cFpHwq8r9ktDGpq46"

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

scrape = ScapeData()

data_entry = DataEntry(driver=driver, link=google_form_url)

for i in range(len(scrape.address)):
    data_entry.input_data(addr=scrape.address[i], price=scrape.price[i], link=scrape.link[i])