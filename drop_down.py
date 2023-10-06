import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")

drop_list = driver.find_elements(By.XPATH, '//option')
drop_menu = driver.find_element(By.ID, 'dropdown').click()

for option in drop_list:
    option.click()
    assert option.is_selected(), f"option {option} was not selected properly"
    time.sleep(1)

time.sleep(3)