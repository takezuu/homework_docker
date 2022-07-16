from page_objects.ProductPage import ProductPage
import allure


@allure.feature('Product page')
@allure.title('Check the like button')
def test_clickable_of_like_button(browser, base_url):
    '''Clickable test'''
    ProductPage(browser).open_url(base_url, ProductPage.PATH)
    ProductPage(browser).check_clickable(ProductPage.CLICKABLE_ELEMENT)


@allure.feature('Product page')
@allure.title('Check the right column')
def test_right_sidebar_visibility_of_all_elements(browser, base_url):
    '''Visibility of all elements test'''
    ProductPage(browser).open_url(base_url, ProductPage.PATH)
    ProductPage(browser).check_visibility_of_all_elements_located(ProductPage.VISIBILITY_ELEMENTS)


@allure.feature('Product page')
@allure.title('Check image')
def test_presence_of_image(browser, base_url):
    '''Presence of image test'''
    ProductPage(browser).open_url(base_url, ProductPage.PATH)
    ProductPage(browser).check_presence_of_element(ProductPage.PRESENCE_ELEMENT)


@allure.feature('Product page')
@allure.title('Check add to cart button')
def test_visibility_of_add_to_cart_button(browser, base_url):
    '''Visibility of test'''
    ProductPage(browser).open_url(base_url, ProductPage.PATH)
    ProductPage(browser).check_visibility_of_element(ProductPage.VISIBILITY_ELEMENT)


@allure.feature('Product page')
@allure.title('Check upload file button\'s attribute')
def test_upload_file_button_for_element_attribute(browser, base_url):
    '''For element attribute test'''
    ProductPage(browser).open_url(base_url, ProductPage.PATH)
    ProductPage(browser).check_element_attribute(ProductPage.ELEMENT_ATTRIBUTE)
