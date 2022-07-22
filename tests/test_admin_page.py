from page_objects.AdminPage import AdminPage
import allure
import config


@allure.feature('Authorization form')
@allure.title('Check the login button')
def test_clickable_of_login_button(browser, base_url):
    AdminPage(browser).open_url(base_url, AdminPage.PATH)
    AdminPage(browser).check_clickable(AdminPage.CLICKABLE_ELEMENT)


@allure.feature('Authorization form')
@allure.title('Check all elements of the login panel')
def test_of_all_elements_login_panel(browser, base_url):
    AdminPage(browser).open_url(base_url, AdminPage.PATH)
    AdminPage(browser).check_visibility_of_all_elements_located(AdminPage.VISIBILITY_ELEMENTS)
