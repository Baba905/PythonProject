from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Firefox()
driver.get("https://tinder.com/")


email = "" \
        ""
password =""

connexion = driver.find_element(By.LINK_TEXT, value="Connexion")
connexion.click()
sleep(5)
facebook = driver.find_element(By.CSS_SELECTOR, value="div.My\(12px\):nth-child(2) > button:nth-child(1)")
facebook.click()
# sleep(10)
# cookies = driver.find_element(By.CSS_SELECTOR,value='button[title="Refuser les cookies optionnels"]')
# cookies.click()

sleep(10)

email_input = driver.find_element(By.CSS_SELECTOR, value='input#email.inputtext._55r1')
email_input.send_keys(email)
password_input = driver.find_element(By.CSS_SELECTOR, value="#pass")
connect_button = driver.find_element(By.CSS_SELECTOR, value="#u_0_0_P0")
connect_button.click(Keys.ENTER)
