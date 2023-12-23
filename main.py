from pprint import pprint
from scrapping import Scrapping
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# ################################################# SCRAPPING PART ######################################################
scrapping = Scrapping()
scrapping.set_prices()
scrapping.set_address()
scrapping.set_links()
#print(f"Adrdress : {scrapping.address}\nPrice : {scrapping.prices}\nLink :{scrapping.links}")

####################################### SELENIUM PART ########################################################

driver = webdriver.Firefox()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfq7FCOPrJumBYXJvb-zJqn38GV7Qhk48V9JDR2csdAHBiEQg/viewform")



for (address, price, link) in zip(scrapping.address,scrapping.prices,scrapping.links):
    address_input = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    address_input.send_keys(address)
    sleep(2)
    price_input = driver.find_element(By.XPATH,value="//div[@role='list']//div[2]//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]//div[1]//input[1]")
    price_input.send_keys(price)
    sleep(2)
    link_input = driver.find_element(By.XPATH, value="//div[@class='teQAzf']//div[3]//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]//div[1]//input[1]")
    link_input.send_keys(link)
    sleep(2)
    send_button = driver.find_element(By.XPATH, value="//div[@class='uArJ5e UQuaGc Y5sE8d VkkpIf QvWxOd']")
    send_button.click()
    sleep(2)
    new_reponse = driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    new_reponse.click()
