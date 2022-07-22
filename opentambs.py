from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#Step 1: open stocks tabs
driver.get("https://www.tradingview.com/markets/stocks-china/market-movers-all-stocks/")
wait = WebDriverWait(driver, 10)

#save the main tab in a variable
original_windows = driver.current_window_handle

#check that there is only one tab open
assert len(driver.window_handles) == 1

#I creat a list to try it
lista = ["000001", "000002"]

#this loop will go through the list elements and click them
for click in lista:
    driver.find_element(By.LINK_TEXT, click).click()
    wait.until(EC.number_of_windows_to_be(2))
    
    # chane tab loop
    for window_handle in driver.window_handles:
        if window_handle != original_windows:
            driver.switch_to.window(window_handle)
            break
    
    # apply an accion inside the second tab, stay 5 secods and close
    financial = driver.find_element(By.LINK_TEXT, "Financials").click()
    time.sleep(5)
    driver.close()
    #return to the main tab to keep going through the list.
    driver.switch_to.window(original_windows)
       
driver.quit()  


    