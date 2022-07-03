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

# driver.get("https://www.tradingview.com/markets/stocks-china/market-movers-all-stocks/")
# print(driver.title)
# driver.quit()
def run():
    print("""
          1st = We will introduce a webpage link and 
          this software will read a scrap the information
          that we need to do a stock fundamental analyst
          """)
    
    url = input("Introduce an URL from Trading View: ")
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, "html.parser")
    print(soup)
    
    urls={}
    for link in soup.find_all('a'):
        print(link.get('href'))
        
        
    
if __name__ == "__main__":
    run()
