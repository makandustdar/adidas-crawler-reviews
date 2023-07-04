from selenium.webdriver.common.by import By


def cookie_handler(driver):
    signin_div = driver.find_elements(By.ID, "account-portal-modal")
    if signin_div:
        btn = signin_div[0].find_elements(By.NAME, "account-portal-close")
        if btn:
            btn[0].click()

    cookie_div = driver.find_elements(By.ID, "gl-modal__cookie-consent-modal")
    if cookie_div:
        btn = cookie_div[0].find_elements(By.ID, "glass-gdpr-default-consent-accept-button")
        if btn:
            btn[0].click()

