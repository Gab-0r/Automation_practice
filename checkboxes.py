from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(0.5)
checkboxes = driver.find_elements(By.XPATH, "//form[@id='checkboxes']/input[@type='checkbox']")

for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()

for checkbox in checkboxes:
    assert checkbox.is_selected(), "A check box is not working correctly"

for checkbox in checkboxes:
    checkbox.click()

assert not checkbox.is_selected(), "A check box is not working correctly"



time.sleep(2)