from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("http://secure-retreat-92358.herokuapp.com/")

# anchor = driver.find_element(By.CSS_SELECTOR, value="a[title ='Special:Statistics']")
# print(anchor.text)
# anchor.click()
# all_portals = driver.find_element(By.LINK_TEXT,"Community portal")
# all_portals.click()
# driver.close()

# Fill a form

first_name =driver.find_element(By.NAME, value="fName")
first_name.send_keys("Baba")
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Diop")
email = driver.find_element(By.NAME, value="email")
email.send_keys('babadiop@gmail.com')
button = driver.find_element(By.TAG_NAME, value="button")
button.send_keys(Keys.ENTER)