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
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
import re

def run():
    print("""
          1st = We will introduce a webpage link and 
          this software will read a scrap the information
          that we need to do a stock fundamental analyst
          """)
    
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    #Step 1: open stocks tabs
    driver.get("https://www.tradingview.com/markets/stocks-china/market-movers-all-stocks/")
    
    actions = ActionChains(driver)
    
    stock_numbers = list()
    for i in range(47):
        load_button = driver.find_element(By.CLASS_NAME, "loadButton-59hnCnPW")
        actions.click(load_button)
        actions.perform()
        time.sleep(6)
            
    all_stocks = driver.find_element(By.CLASS_NAME, "js-screener-markets-page-init-ssr")
    all_stocks = all_stocks.text.split()
    
    for quotes in all_stocks:
        if re.findall("^.*([0-9]{6}).*$", quotes):
            stock_numbers.append(quotes)
            
    print(stock_numbers)
    
    for click in stock_numbers:
        click_shares = driver.find_element(By.LINK_TEXT, click)
        actions.click(click_shares)
        actions.perform()
    
    # Make the web browser to wait until it opens the new tab
    try:
    
        all_stocks = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "js-screener-markets-page-init-ssr")))
        print(all_stocks)
        
    except:
        driver.quit()
    
if __name__ == "__main__":
    run()