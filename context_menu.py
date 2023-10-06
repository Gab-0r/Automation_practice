from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver = Chrome()
actionsChains = ActionChains(driver)

driver.get("https://the-internet.herokuapp.com/context_menu")
box = driver.find_element(By.ID, "hot-spot")
actionsChains.context_click(box).perform()

try:
    WebDriverWait(driver, 2).until(EC.alert_is_present())
    alert = driver.switch_to.alert
except TimeoutException:
    print("Alert does not exist")
else:
    alert.accept()
    print("Alert exist")
time.sleep(2)