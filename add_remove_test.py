import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
def add_remove_test(n: int):
    buttonList=  []
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

    #Click add button n times
    for i in range(n):
        try:
            add_button = driver.find_element(By.CSS_SELECTOR, "button[onClick='addElement()'")
        except:
            print("add button not found")
        else:
            add_button.click()
        time.sleep(0.5)

    #Check if the n delete buttons were added
    try:
        buttonList = driver.find_elements(By.XPATH, "//div[@id='elements']/button")
    except:
        print("buttons added not found")
    else:
        assert len(buttonList) == n, "Not added the required number of buttons"
        delete_buttons_test(buttonList)

def delete_buttons_test(buttonList: list):
    #clicking each button
    for deleteButton in buttonList:
        deleteButton.click()
        time.sleep(0.5)
    #check if the buttons were deleted
    try:
        driver.find_element(By.CSS_SELECTOR, "//div[@id='elements'/button")
    except:
        print("Buttons were sucessfully deleted")
    else:
        print("Buttons were not deleted successfully")


add_remove_test(12)
time.sleep(2)