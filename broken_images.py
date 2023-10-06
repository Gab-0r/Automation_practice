import time
import requests
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


driver = Chrome()

def find_broken_img():
    driver.get("https://the-internet.herokuapp.com/broken_images")
    images = driver.find_elements(By.XPATH, "//div[@class='example']/img")
    #Make a get request to each src image attribute
    for image in images:
        response = requests.get(image.get_attribute('src'))
        assert response.status_code == 200, "Broken imagen found"

def find_broken_img_good():
    driver.get("https://the-internet.herokuapp.com/broken_images")
    images = driver.find_elements(By.XPATH, "(//div[@class='example']/img)[3]")
    for image in images:
        response = requests.get(image.get_attribute('src'))
        assert response.status_code == 200, "Broken imagen found"

find_broken_img()
find_broken_img_good()
time.sleep(2)