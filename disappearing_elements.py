import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def check_elements(n: int):
    expected_elements = ["Home", "About", "Contact Us", "Portfolio", "Gallery"]
    driver = Chrome()
    for i in range(n):
        driver.get("https://the-internet.herokuapp.com/disappearing_elements")

        real_elements = driver.find_elements(By.XPATH, "//div[@class='example']/ul/li/a")
        text_elements= [element.text for element in real_elements]
        time.sleep(3)
        for element in expected_elements:
            assert element in text_elements, f"{element} element does not show correctly"
        print("menu is complete")

check_elements(3)