from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class ProductPage(BasePage):

    PATH = 'desktops/test'
    CLICKABLE_ELEMENT = (By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")
    VISIBILITY_ELEMENTS = (By.CSS_SELECTOR, "#content div .col-sm-4")
    PRESENCE_ELEMENT = (By.CSS_SELECTOR, ".image-additional a img")
    VISIBILITY_ELEMENT = (By.CSS_SELECTOR, "#button-cart")
    ELEMENT_ATTRIBUTE = ((By.CSS_SELECTOR, "#button-upload222"), 'data-loading-text')
