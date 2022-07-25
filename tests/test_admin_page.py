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


@allure.feature('Authorization form')
@allure.title('Check the link')
def test_presence_of_open_cart_link(browser, base_url):
    AdminPage(browser).open_url(base_url, AdminPage.PATH)
    AdminPage(browser).check_presence_of_element(AdminPage.PRESENCE_ELEMENT)


@allure.feature('Authorization form')
@allure.title('Check the login field')
def test_visibility_of_login_field(browser, base_url):
    AdminPage(browser).open_url(base_url, AdminPage.PATH)
    AdminPage(browser).check_visibility_of_element(AdminPage.VISIBILITY_ELEMENT)


@allure.feature('Authorization form')
@allure.title('Check the password field')
def test_password_field_for_element_attribute(browser, base_url):
    AdminPage(browser).open_url(base_url, AdminPage.PATH)
    AdminPage(browser).check_element_attribute(AdminPage.ELEMENT_ATTRIBUTE)


@allure.feature('Admin panel')
@allure.title('Add a new product')
def test_add_new_product_admin_panel(browser, base_url):
    AdminPage(browser).open_url(base_url, AdminPage.PATH)
    AdminPage(browser).log_in(config.LOGIN, config.PASSWORD)
    AdminPage(browser).add_new_product(AdminPage.product_name, AdminPage.meta_teg, AdminPage.product_model)
    product_name = AdminPage(browser).check_new_product(AdminPage.product_name)
    assert product_name == AdminPage.product_name, 'Продукт не добавлен'


@allure.feature('Admin panel')
@allure.title('Delete a product')
def test_delete_product_admin_panel(browser, base_url):
    AdminPage(browser).open_url(base_url, AdminPage.PATH)
    AdminPage(browser).log_in(config.LOGIN, config.PASSWORD)
    AdminPage(browser).add_new_product(AdminPage.product_name_2, AdminPage.meta_teg, AdminPage.product_model)
    AdminPage(browser).check_new_product(AdminPage.product_name)
    delete_text = AdminPage(browser).delete_product()
    assert delete_text == 'Success: You have modified products!\n×', 'Товар не удален'
