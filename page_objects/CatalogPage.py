from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class CatalogPage(BasePage):

    PATH = 'desktops'
    CLICKABLE_ELEMENT = (By.CSS_SELECTOR, "#list-view")
    VISIBILITY_ELEMENTS = (By.CSS_SELECTOR, "#content")
    PRESENCE_ELEMENT = (By.CSS_SELECTOR, "footer")
    VISIBILITY_ELEMENT = (By.CSS_SELECTOR, "#column-left")
    ELEMENT_ATTRIBUTE = ((By.CSS_SELECTOR, "#content div div img"), 'class')
