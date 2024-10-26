import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.vetementpro.com/433-tenues-spa-bien-etre"

driver.get(url)

time.sleep(3)

tenues = driver.find_elements(By.CLASS_NAME, "product-description")
parsed_data = []

for tenue in tenues:
    try:
        title = tenue.find_element(By.CSS_SELECTOR, "h2.h3").text
        price = tenue.find_element(By.CSS_SELECTOR, "span.price").text
        url = tenue.find_element(By.CSS_SELECTOR, "a").get_attribute("href")

    except:
        print("error")
        continue

    parsed_data.append([title, price, url])

driver.quit()

with open("tenues.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Название продукта", "Цена продккта", "Ссылка на продукт"])
    writer.writerows(parsed_data)






