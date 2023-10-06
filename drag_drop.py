import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = Chrome()
driver.get("https://the-internet.herokuapp.com/drag_and_drop")

a_box = driver.find_element(By.ID, "column-a")
b_box = driver.find_element(By.ID, "column-b")

action = ActionChains(driver)
action.drag_and_drop(a_box, b_box).perform()

time.sleep(2)