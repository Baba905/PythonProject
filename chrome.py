from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Create and configure driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

# Launch browser
driver.get(url="https://tinder.com/app/recs")
driver.implicitly_wait(10)


email = ""
password =""

connexion = driver.find_element(By.LINK_TEXT, value="Connexion")
connexion.click()