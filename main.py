from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from decouple import config

from core.cookie import cookie_handler
from core.fetch_reviews import get_reviews

# Check debug mode True/False
DEBUG_MODE = config('DEBUG_MODE')
if DEBUG_MODE == 'True':
    DEBUG_MODE = True
else:
    DEBUG_MODE = False


def main():
    # Make driver chrome with selenium
    driver = webdriver.Chrome()
    driver.get("https://www.adidas.com/us/search?q=")

    # Close Adidas club popup and cookie
    cookie_handler(driver)

    products_box = driver.find_element(By.CLASS_NAME, 'plp-grid___1FP1J')
    all_items = products_box.find_elements(By.CLASS_NAME, "grid-item")

    # Witting for get all products
    time.sleep(3)

    for item in all_items:
        while True:
            try:
                url = item.find_element(By.CLASS_NAME, "glass-product-card__assets").find_element(
                    By.TAG_NAME, "a"
                ).get_attribute('href')
                break
            except Exception as e:
                print(e)
                time.sleep(1)

        driver.execute_script(f"window.open('{url}');")

        # Switch to the new window
        driver.switch_to.window(driver.window_handles[1])

        # Close Adidas club and cookie

        cookie_handler(driver)

        while True:
            review_div = driver.find_elements(By.ID, "navigation-target-reviews")
            if len(review_div) > 0:
                break
        review_div[0].click()

        get_reviews(url=url,driver=driver,debug_mode=DEBUG_MODE)

        driver.get(url)
        time.sleep(3)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])


if __name__ == "__main__":
    main()
    # get_reviews(url="https://www.adidas.com/us/classic-3-stripes-backpack/EX6516.html", directed=True)
