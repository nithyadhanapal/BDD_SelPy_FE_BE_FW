import time

from behave import given, when, then
from BDDCommon.CommonConfigs.locatorConfigs import CHECKOUT_PAGE_LOCATORS
from BDDCommon.CommonFuncs import driver_functions
from BDDCommon.CommonHelpers.utilitiesHelper import generate_random_email_password
from BDDCommon.CommonHelpers.utilitiesHelper import generate_random_fnama_lname

@when("I verify 'checkout' page is loaded")
def i_verify_checkout_page_is_loaded(context):

    # check the heading text
    checkout_title_locator_type = CHECKOUT_PAGE_LOCATORS['checkout_title']['type']
    checkout_title_locator = CHECKOUT_PAGE_LOCATORS['checkout_title']['locator']

    expected_text = 'Checkout'
    contains = driver_functions.element_contains_text(context, expected_text, checkout_title_locator_type,checkout_title_locator)
    assert contains, f"Header of checkout page does not contain the text '{expected_text}'."

    # Check some elements are visible
    checkout_form_locator_type = CHECKOUT_PAGE_LOCATORS['checkout_form']['type']
    checkout_form_locator= CHECKOUT_PAGE_LOCATORS['checkout_form']['locator']

    driver_functions.assert_element_visible(context, checkout_form_locator_type, checkout_form_locator)

@when("I fill in the billing details form")
def i_fill_in_the_billing_details_form(context):
    rand_fname = generate_random_fnama_lname()
    f_name = rand_fname['first_name']
    l_name = rand_fname['last_name']
    _country = 'USA'
    _address = 'Concord ave'
    _city = 'Boston'
    _state = 'MA'
    _zip_code = '12344'
    _phone_number = '123455677'
    _email = generate_random_email_password()['email']

    first_name = CHECKOUT_PAGE_LOCATORS['first_name']
    last_name = CHECKOUT_PAGE_LOCATORS['last_name']
    country = CHECKOUT_PAGE_LOCATORS['country']
    address = CHECKOUT_PAGE_LOCATORS['address']
    city = CHECKOUT_PAGE_LOCATORS['city']
    state = CHECKOUT_PAGE_LOCATORS['state']
    zip_code = CHECKOUT_PAGE_LOCATORS['zip_code']
    phone_number = CHECKOUT_PAGE_LOCATORS['phone_number']
    email = CHECKOUT_PAGE_LOCATORS['email']

    driver_functions.type_into_element(context, f_name, first_name['type'], first_name['locator'])
    driver_functions.type_into_element(context, l_name, last_name['type'], last_name['locator'])
    # driver_functions.type_into_element(context, _country, country['type'], country['locator'])
    driver_functions.type_into_element(context, _address, address['type'], address['locator'])
    driver_functions.type_into_element(context, _city, city['type'], city['locator'])
    # driver_functions.type_into_element(context, _state, state['type'], state['locator'])
    driver_functions.type_into_element(context, _zip_code, zip_code['type'], zip_code['locator'])
    driver_functions.type_into_element(context, _phone_number, phone_number['type'], phone_number['locator'])
    driver_functions.type_into_element(context, _email, email['type'], email['locator'])


@when("I click on 'Place order' button in the checkout page")
def i_click_on_place_order_button_in_the_checkout_page(context):
    time.sleep(1)
    place_order = CHECKOUT_PAGE_LOCATORS['place_order_btn']
    driver_functions.click(context, place_order['type'], place_order['locator'])



