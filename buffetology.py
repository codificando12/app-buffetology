import os
import time
from turtle import title
import selenium
import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
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
    
    driver.get("https://www.tradingview.com/symbols/SZSE-300750/")
    header = driver.find_element(By.CLASS_NAME, "tv-symbol-header__first-line").text
    
    #This line will get the stock number and rate return.
    
    # share_number = header.rsplit()[6]
    # stock_price = float(header.rsplit()[22])
    # eps = float(header.rsplit()[39])
    # rate_return = "The rate return for this share is\n" + str(round((eps / stock_price), 2) * 100) + "%"
    print(header)
    
    driver.quit()  

    

if __name__ == "__main__":
    run()
