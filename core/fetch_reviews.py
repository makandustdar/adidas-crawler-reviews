import json

from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from core.cookie import cookie_handler


def get_reviews(url, driver=None, debug_mode=False, directed=False):
    if directed:
        from selenium import webdriver
        driver = webdriver.Chrome()
        driver.get(url)
    cookie_handler(driver)

    result = {
        'items': [],
        'count': 0,
        'url': url
    }
    is_reviews = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "accordion-title___2sTgR")))

    if is_reviews.text != "Reviews":
        reviews_count = int(is_reviews.text.split('(')[1].replace(')', ''))
        is_reviews = True
    else:
        reviews_count = 0
        is_reviews = False

    if is_reviews:
        while True:
            reviews_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "navigation-target-reviews")))
            reviews_btn.click()
            reviews_box = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "reviews___3fzxE"))
            )
            reviews = reviews_box.find_elements(By.TAG_NAME, "article")

            if result['count'] >= 0:
                reviews = reviews[result['count']:]
            for item in reviews:
                try:
                    text = item.find_element(By.CLASS_NAME, "review-text-container___3llE0").find_element(
                        By.TAG_NAME, 'div'
                    ).text

                    rate = 0
                    for i in item.find_elements(By.CLASS_NAME, "gl-star-rating__mask"):
                        if '88' in i.get_attribute('style'):
                            rate += 1
                    if not text:
                        break
                    result['items'].append({
                        'text': text,
                        'rate': rate
                    })
                    if debug_mode:
                        print({
                            'text': text,
                            'rate': rate
                        })
                    result['count'] += 1
                except StaleElementReferenceException:
                    print("88")
            # Make result file as .json
            json_object = json.dumps(result, indent=4)
            with open("sample.json", "w") as outfile:
                outfile.write(json_object)
                outfile.close()

            try:
                read_more_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="bazaarvoice-container"]/div/div[1]/button'))
                )
                read_more_box.click()
                if debug_mode:
                    print(result['count'])
                if result['count'] >= reviews_count:
                    break
            except:
                return
