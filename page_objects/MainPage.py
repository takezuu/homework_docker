from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
import allure

class MainPage(BasePage):
    CLICKABLE_ELEMENT = (By.CSS_SELECTOR, "#cart button")
    VISIBILITY_ELEMENTS = (By.CSS_SELECTOR, '.row')
    PRESENCE_ELEMENT = (By.CSS_SELECTOR, ".btn-group button")
    VISIBILITY_ELEMENT = (By.CSS_SELECTOR, ".collapse.navbar-collapse.navbar-ex1-collapse")
    ELEMENT_ATTRIBUTE = ((By.CSS_SELECTOR, ".swiper-container.swiper-container-horizontal"), 'id')

    @allure.step('Open reg form')
    def open_reg_form(self):
        try:
            self.browser.find_element(By.CSS_SELECTOR, ".dropdown").click()
            self.browser.find_element(By.CSS_SELECTOR, ".dropdown.open > ul > li > a").click()
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='open_reg_form')

    @allure.step('Define currency')
    def define_currency(self):
        try:
            return self.browser.find_element(By.CSS_SELECTOR, ".btn.btn-link.dropdown-toggle > strong").text
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='define_currency')

    @allure.step('Change currency')
    def change_currency(self):
        try:
            self.browser.find_element(By.CSS_SELECTOR, ".btn-group").click()
            self.browser.find_element(By.CSS_SELECTOR, ".btn-group.open > ul > li > [name ='EUR']").click()
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='change_currency')