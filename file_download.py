import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/download")
try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((
        By.XPATH, "//div[@class='example']/a"
    )))
except:
    print("Element was not located")
else:
    element = driver.find_element(By.XPATH, "//div[@class='example']/a")
    text = element.text
    element.click()
    time.sleep(5)
    Path(f"/Users/juan.orozco/Downloads/{text}").rename(f"/Users/juan.orozco/Desktop/Automation practice/Automation_practice/{text}")
    time.sleep(2)