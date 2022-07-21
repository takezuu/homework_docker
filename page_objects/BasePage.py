from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, InvalidArgumentException
import allure


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def open_url(self, base_url, path=''):
        try:
            self.browser.get(base_url + path)
        except InvalidArgumentException:
            raise AssertionError("Не открылся url")

    def check_clickable(self, clickable_element):
        try:
            WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(clickable_element))
        except TimeoutException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='clickable_element')
            raise AssertionError("Не дождалcя возможности клика по кнопке")

    def check_visibility_of_all_elements_located(self, visibility_elements):
        try:
            WebDriverWait(self.browser, 5).until(EC.visibility_of_all_elements_located(visibility_elements))
        except TimeoutException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='visibility_of_all_elements')
            raise AssertionError("Не дождалcя видимости элемента")

    def check_presence_of_element(self, presence_element):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(presence_element))
        except TimeoutException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='presence_of_element_located')
            raise AssertionError("Не дождалcя присутствия элемента на странице")

    def check_visibility_of_element(self, visibility_element):
        try:
            WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(visibility_element))
        except TimeoutException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='visibility_element')
            raise AssertionError("Не дождалcя видимости элемента на странице")

    def check_element_attribute(self, element_attribute):
        try:
            WebDriverWait(self.browser, 5).until(EC.element_attribute_to_include(*element_attribute))
        except TimeoutException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='element_attribute')
            raise AssertionError("Отсутствует атрибут")
