from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By

driver = Chrome()
user = "admin"
password = "admin"
driver.get(f"https://{user}:{password}@the-internet.herokuapp.com/basic_auth")

try:
    driver.find_element(By.XPATH, "//div[@class='example']/p")
except:
    print("Incorrect credentials")
else:
    print("User logged successfully")


time.sleep(2)