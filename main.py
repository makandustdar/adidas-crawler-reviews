from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://www.adidas.com/us/search?q=")


cooki_div= driver.find_elements(By.ID, "gl-modal__cookie-consent-modal")
if (len(cooki_div)):
    btn=cooki_div[0].find_elements(By.TAG_NAME, "button")
    btn[0].click()

signin_div= driver.find_elements(By.CLASS_NAME, "gl-modal__dialog gl-modal__dialog--small")
if (len(signin_div)):
    btn=signin_div[0].find_elements(By.NAME, "account-portal-close")
    btn[0].click()



#switch to alert box
# alert = driver.switch_to.alert

#sleep for a second
# time.sleep(1)

#accept the alert
# alert.accept()

# dismiss the alert
# alert.dismiss()

products_box = driver.find_element(By.CLASS_NAME, 'plp-grid___1FP1J')
all_items = products_box.find_elements(By.CLASS_NAME, "grid-item")


for item in all_items:
    url = item.find_element(By.CLASS_NAME, "glass-product-card__assets").find_element(By.TAG_NAME, "a").get_attribute(
        'href')
    # input()
    driver.execute_script("window.open('');")
    # Switch to the new window
    driver.switch_to.window(driver.window_handles[1])
    while(True):
        review_div= driver.find_elements(By.ID, "navigation-target-reviews")
        # btn=review_div.find_elements(By.TAG_NAME, "button")
        # btn[0].click()
        if (len(review_div)>0):
            break
    review_div[0].click()


    driver.get(url)
 
    time.sleep(3)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])