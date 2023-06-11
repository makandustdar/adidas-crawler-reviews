from selenium import webdriver
from selenium.webdriver.common.by import By

import csv

driver = webdriver.Chrome()
driver.get("https://www.adidas.com/us/samba-og-shoes/B75807.html")

is_reviews = driver.find_element(By.CLASS_NAME, "accordion-title___2sTgR")
if is_reviews.text != "Reviews":
    is_reviews = True
else:
    is_reviews = False

while True:
    reviews_box = driver.find_element(By.CLASS_NAME, "reviews___3fzxE")
    reviews = reviews_box.find_elements(By.TAG_NAME, "article")
    counter = 0

    if counter >= 0:
        reviews = reviews[counter:]
    for item in reviews:
        text = item.find_element(By.CLASS_NAME, "review-text-container___3llE0").find_element(By.TAG_NAME, 'div').text

        rate = 0
        for i in item.find_elements(By.CLASS_NAME, "gl-star-rating__mask"):
            if '88' in i.get_attribute('style'):
                rate += 1
        if not text:
            break

        with open('employee_file2.csv', mode='w') as csv_file:
            fieldnames = ['text', 'rate']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({
                'text': text,
                'rate': rate
            })
            print({
                'text': text,
                'rate': rate
            })
        counter += 1
    read_more_box = reviews_box.find_element(By.XPATH, '//*[@id="bazaarvoice-container"]/div/div[1]/button')
    read_more_box.click()
