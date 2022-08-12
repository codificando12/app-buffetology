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
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#Step 1: open stocks tabs
driver.get("https://www.tradingview.com/symbols/SZSE-001203/financials-income-statement/")
wait = WebDriverWait(driver, 10)

# financial = driver.find_element(By.LINK_TEXT, "Financials").click()
# statement = driver.find_element(By.LINK_TEXT, "Statements").click()
# income = driver.find_element(By.LINK_TEXT, "Income statements").click()
time.sleep(5)


try:
    last_eps = driver.find_element(By.XPATH, '//div[@class="container-Odj0lQp6"]/div[20]/div[5]/div[7]/div[1]/div[1]')
    last_eps = last_eps.text
    print(last_eps)
except:
    try:
        last_eps = driver.find_element(By.XPATH, '//div[@class="container-Odj0lQp6"]/div[20]/div[5]/div[6]/div[1]/div[1]')
        last_eps = last_eps.text
        print(last_eps)
    except:
        try:
            last_eps = driver.find_element(By.XPATH, '//div[@class="container-Odj0lQp6"]/div[20]/div[5]/div[5]/div[1]/div[1]')
            last_eps = last_eps.text
            print(last_eps)
        except:
            try:
                last_eps = driver.find_element(By.XPATH, '//div[@class="container-Odj0lQp6"]/div[20]/div[5]/div[4]/div[1]/div[1]')
                last_eps = last_eps.text
                print(last_eps)
            except:
                try:
                    last_eps = driver.find_element(By.XPATH, '//div[@class="container-Odj0lQp6"]/div[20]/div[5]/div[3]/div[1]/div[1]')
                    last_eps = last_eps.text
                    print(last_eps)
                except:
                    try:
                        last_eps = driver.find_element(By.XPATH, '//div[@class="container-Odj0lQp6"]/div[20]/div[5]/div[2]/div[1]/div[1]')
                        last_eps = last_eps.text
                        print(last_eps)
                    except:
                        last_eps = driver.find_element(By.XPATH, '//div[@class="container-Odj0lQp6"]/div[20]/div[5]/div[1]/div[1]/div[1]')
                        last_eps = last_eps.text
                        print(last_eps)
    



# elif last_eps == False and driver.find_element(By.XPATH, '//div[@class="container-Odj0lQp6"]/div[20]/div[5]/div[4]/div[1]/div[1]') == True:
    # print("The last EPS is: " + last_eps)