import os
import time
import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd

def run():
    print("""
          1st = We will introduce a webpage link and 
          this software will read a scrap the information
          that we need to do a stock fundamental analyst
          """)
    
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    
    driver.get("https://www.tradingview.com/symbols/SSE-601398/financials-overview/")
    driver.find_element
    #proximo paso : tratar de extraer el precio de la accion y el EPS
    
    # tv-category-header__price-line
      
    eps = 
    print(url)
    
    while True:
        sleep(1)
if __name__ == "__main__":
    run()
