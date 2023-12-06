from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("https://www.python.org/")

li_tag = driver.find_elements(By.CSS_SELECTOR, value=".medium-widget.event-widget.last li")


length = len(li_tag)
data = {}

for i in range(length):
    anchor = li_tag[i].find_element(By.TAG_NAME, value="a").text
    time = li_tag[i].find_element(By.TAG_NAME, value="time").get_attribute("datetime").split("T")[0]
    data[f"{i}"] = {'time': time, 'name': anchor}
print(data)

driver.close()