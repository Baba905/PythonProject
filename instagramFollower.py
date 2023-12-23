from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

SIMILAR_ACCOUNT = "chefsteps"
USERNAME = ""
PASSWORD = ""

class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(5)
        decline_cookies = self.driver.find_element(By.XPATH,value="/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]")
        decline_cookies.click()
        sleep(5)

        username_input = self.driver.find_element(By.XPATH,value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
        username_input.send_keys(USERNAME)

        password_input = self.driver.find_element(By.XPATH,value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
        password_input.send_keys(PASSWORD)

        login_buuton = self.driver.find_element(By.XPATH,value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
        login_buuton.click()

        sleep(5)
        self.driver.find_element(By.XPATH,value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div").click()
        # later_button.click()
        sleep(5)
        self.driver.find_element(By.XPATH,value="/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()

    def find_followers(self):
        self.driver.get("https://www.instagram.com/manchesterunited/")
        sleep(10)
        followers_page = self.driver.find_element(By.XPATH,value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")
        followers_page.click()
        sleep(10)
        scroll = self.driver.find_element(By.CSS_SELECTOR, value="._aano")

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            sleep(2)
    def follow(self):

        buttons = self.driver.find_elements(By.CSS_SELECTOR, value="._aano button")

        for button in buttons:
            try:
                button.click()
                sleep(2)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()