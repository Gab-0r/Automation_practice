import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

driver = Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading")
driver.find_element(By.XPATH, "//div[@class='example']/a[1]").click()

start_button = driver.find_element(By.XPATH, "//div[@id='start']/button")
start_button.click()
try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@id='finish']/h4")))
except TimeoutException:
    print("the title was not appear")
else:
    print("the title appear correctly")

time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.XPATH, "//div[@class='example']/a[2]").click()

start_button = driver.find_element(By.XPATH, "//div[@id='start']/button")
start_button.click()
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='finish']/h4")))
except TimeoutException:
    print("the title was not appear")
else:
    print("the title appear correctly")


time.sleep(2)