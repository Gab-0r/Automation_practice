from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()
driver.get("https://the-internet.herokuapp.com/exit_intent")


time.sleep(2)