from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

TWITTER_EMAIL = "bdiop8683@gmail.com"
TWITTER_PASSWORD = "loveTKD99++"

class InternetTwitterBot:
    def __init__(self,):
        self.driver = webdriver.Firefox()
        self.down=0
        self.up =0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        star_button = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
        star_button.click()
        sleep(60)
        down = self.driver.find_element(By.XPATH,value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        up = self.driver.find_element(By.XPATH,value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        self.down = float(down)
        self.up  = float(up)
        self.driver.quit()


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")

        # Log in in twitter (X)
        sleep(5)
        email_input = self.driver.find_element(By.XPATH, value="//input[@name='text']")
        email_input.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(By.XPATH,value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()
        sleep(5)
        username = self.driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
        username.send_keys("bdiop8683")
        next_button_username = self.driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div")
        next_button_username.click()

        sleep(15)
        password_input = self.driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password_input.send_keys(TWITTER_PASSWORD)
        login_button = self.driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")
        login_button.click()

        sleep(15)
        # Post on twitter (X)
        post_button = self.driver.find_element(By.XPATH, value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]")
        post_button.click()
        sleep(5)
        post_input = self.driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div")
        post_input.send_keys(f'@AbouM_D, project work\n Dowload : {self.down}\nUpload:{self.up}')
        sleep(5)
        post_input_button = self.driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]")
        post_input_button.click()
        self.driver.quit()
