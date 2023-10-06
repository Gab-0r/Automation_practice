from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver = Chrome()

driver.get("https://the-internet.herokuapp.com/entry_ad")

try:
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='modal']")))
except TimeoutException:
    print("modal window was not displayed")
else:
    print("modal window was displayed correctly")

time.sleep(1)

driver.find_element(By.XPATH, "//div[@class='modal-footer']/p").click()

try:
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='modal']")))
except TimeoutException:
    print("modal window was closed cosed correctly")
else:
    print("modal window was not closed correctly")

time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "a[id='restart-ad']").click()
driver.get("https://the-internet.herokuapp.com/entry_ad")
try:
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='modal']")))
except TimeoutException:
    print("modal window was not displayed after click re-enable button")
else:
    print("modal window was displayed correctly after click re-enable button")

time.sleep(2)

