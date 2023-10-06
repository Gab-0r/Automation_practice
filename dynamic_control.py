from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver = Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_controls")
def remove_add_test():
    remove_add_button = driver.find_element(By.XPATH, "//button[@onclick='swapCheckbox()']")
    remove_add_button.click()

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//form[@id='checkbox-example']/p")))
    except TimeoutException:
        print("checkbox did not disappear")
    else:
        print("checkbox disappear correctly")

    time.sleep(1)

    remove_add_button.click()

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox']")))
    except TimeoutException:
        print("checkbox did not appear")
    else:
        print("checkbox appear correctly")
def enable_disable_test():
    enable_disable_button = driver.find_element(By.XPATH, "//button[@onclick='swapInput()']")
    enable_disable_button.click()
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//form[@id='input-example']/p")))
    except TimeoutException:
        print("input was not enabled")
    else:
        print("input enabled correctly")

    enable_disable_button.click()
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//p[@id='message']")))
    except:
        print("input was not disabled")
    else:
        print("input disabled correctly")

remove_add_test()
time.sleep(1)
enable_disable_test()