from selenium.webdriver.common.by import By


def get_product_image(driver, ):
    gallery_box = driver.find_element(By.ID, "navigation-target-gallery")
    show_more = gallery_box.find_elements(By.CLASS_NAME, "gl-cta gl-cta--secondary")

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
