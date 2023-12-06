from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("https://www.amazon.fr/Pack-Playstation-PS5-SPORTS-t%C3%A9l%C3%A9chargement/dp/B0CGV4SBDL/?_encoding=UTF8&pd_rd_w=gGRHg&content-id=amzn1.sym.73703761-4b87-4afd-89de-5f39639d96be&pf_rd_p=73703761-4b87-4afd-89de-5f39639d96be&pf_rd_r=826MTT12MZQS0YF5JKND&pd_rd_wg=2CCeq&pd_rd_r=ed135220-3606-4449-8d31-34eec9bc2cd3&ref_=pd_gw_gcx_gw_per_1&th=1")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_dollar = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div[5]/div[5]/div[1]/div[4]/div/div/div/div[1]/div/div/div/form/div/div/div/div/div[3]/div/div[1]/div/div/span[1]/span[2]/span[1]')
price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price of PS5 is {price_dollar.text}.{price_cent.text}")

driver.quit()

