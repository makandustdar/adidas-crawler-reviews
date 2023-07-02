import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.adidas.com/us/classic-3-stripes-backpack/EX6516.html")
button = driver.find_element(By.ID, "navigation-target-gallery")
show_more = button.find_elements(By.CLASS_NAME, "gl-cta gl-cta--secondary")
# print(show_more)
images_url = []
url = [1, 2]

while True:
    # driver.get(i)
    if show_more:
        show_more[0].click()
        container = driver.find_element(By.CLASS_NAME, "image-grid___1JN2z")
        images = container.find_elements(By.TAG_NAME, "img")
        for image in images:
            image = image.get_attribute("src")
            images_url.append(image)
        break
    else:
        container = driver.find_element(By.CLASS_NAME, "image-grid___1JN2z")
        images = container.find_elements(By.TAG_NAME, "img")
        for image in images:
            image = image.get_attribute("src")
            images_url.append(image)
        break

print(images_url)
time.sleep(10000)