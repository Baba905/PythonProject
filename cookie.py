from selenium import webdriver
from selenium.webdriver.common.by import By
import time
item_id =["buyCursor","buyGrandma","buyFactory","buyMine","buyShipment","buyAlchemy lab","buyPortal","buyTime machine"]
def get_prices(driver):
    elements = [driver.find_element(By.ID, value=elt) for elt in item_id]
    prices = [int(elt.find_element(By.TAG_NAME, value="b").text.split("-")[1].replace(",","")) for elt in elements]
    return prices

driver = webdriver.Firefox()
driver.get("http://orteil.dashnet.org/experiments/cookie/")
#


cookie = driver.find_element(By.ID, value="cookie")
money = driver.find_element(By.ID,value="money")
count =0
timeout = time.time()+15
five_minute = time.time() + 5*60
timeover = False

while  not timeover:

    if time.time() < five_minute:
        cookie.click()
        if time.time() > timeout:
            index = 0
            prices = get_prices(driver)
            for price in prices:
                if int(money.text.replace(",", "")) > price:
                    index = prices.index(price)
            driver.find_element(By.ID, value=item_id[index]).click()
            print(f"timeout {timeout}")
            timeout = time.time() + 15
    else:
        timeover =True

driver.quit()


