import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import csv

driver = webdriver.Chrome()
# driver.get("https://www.adidas.com/us/search?q=")
driver.get("https://www.adidas.com/us/samba-og-shoes/B75807.html")

import csv

items = []

while True:
    reviews_box = driver.find_element(By.CLASS_NAME, "reviews___3fzxE")
    reviews = reviews_box.find_elements(By.TAG_NAME, "article")
    counter = 0
    print(reviews)
    if counter >= 0:
        print(len(reviews))
        reviews = reviews[counter:]
    for item in reviews:
        text = item.find_element(By.CLASS_NAME, "review-text-container___3llE0").find_element(By.TAG_NAME, 'div').text

        rate = 0
        for i in item.find_elements(By.CLASS_NAME, "gl-star-rating__mask"):
            if '88' in i.get_attribute('style'):
                rate += 1
        if not text:
            break
        items.append({
            'text': text,
            'rate': rate
        })

        print({
            'text': text,
            'rate': rate
        })
        counter += 1

        if counter >= 30:
            break
    print(counter)

    time.sleep(2)
    if counter >= 30:
        break
    read_more_box = reviews_box.find_element(By.XPATH, '//*[@id="bazaarvoice-container"]/div/div[1]/button')
    read_more_box.click()

    # # read_more = driver.find_element(By.CLASS_NAME, "gl-link gl-body--s gl-no-margin-bottom").click()
    # print(counter)
    # if counter >= 2000:
    #     break

file = open('employee_file2.csv', mode='w')
fieldnames = ['text', 'rate']
writer = csv.DictWriter(file, fieldnames=fieldnames)
writer.writeheader()
writer.writerows(items)
file.close()
