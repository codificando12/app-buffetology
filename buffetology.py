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
    
    driver.get("https://www.tradingview.com/symbols/SSE-601398/")
    #getting the stock number from the title
    stock_number = driver.title
    stock_number = stock_number.rsplit()
    for stock in stock_number:
        if stock.startswith("SZS"):
            stock = stock.split(":")
            print(stock[1])
        elif stock.startswith("BSE"):
            stock = stock.split(":")
            print(stock[1])
        elif stock.startswith("SSE"):
            stock = stock.split(":")
            print(stock[1])
        
        
    # header = driver.find_element(By.ID, "/html/body[@class='search-page]/div[@class='tv-main']/div[@class='tv-content']/div[@id='js-category-content]/header[@id+'anchor-page-1]").text
    
    #This line will get the stock number and rate return.
    
    # share_number = header.rsplit()[6]
    # stock_price = float(header.rsplit()[22])
    # eps = float(header.rsplit()[39])
    # rate_return = "The rate return for this share is\n" + str(round((eps / stock_price), 2) * 100) + "%"
    print(url)
    
    driver.quit()  

    

if __name__ == "__main__":
    run()
