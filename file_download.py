import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

from selenium import webdriver


def download_finish(driver: Chrome):
    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads")
    return driver.execute_script("""
        var items = document.querySelector('downloads-manager')
            .shadowRoot.getElementById('downloadsList').items;
        if (items.every(e => e.state === "COMPLETE"))
            return items.map(e => e.fileUrl || e.file_url);
    """)


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/download")
try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((
        By.XPATH, "//div[@class='example']/a"
    )))
except:
    print("Element was not located")
else:
    element = driver.find_element(By.XPATH, "//div[@class='example']/a")
    text = element.text
    element.click()
try:
    WebDriverWait(driver, 10).until(download_finish)
except:
    print("file was not downloaded")
else:
    Path(f"/Users/juan.orozco/Downloads/{text}").rename(f"/Users/juan.orozco/Desktop/Automation practice/Automation_practice/{text}")
