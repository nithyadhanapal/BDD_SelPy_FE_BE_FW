

from behave import step
from BDDCommon.CommonConfigs.locatorConfigs import HOME_PAGE_LOCATORS
from BDDCommon.CommonFuncs import driver_functions
import random
import time
import logging

@step("I add '{qty}' random item to cart from the homepage")
def i_add_random_item_to_cart_from_homepage(context, qty):

    logging.info(f"Adding {qty} items to the cart")
    cart_btns = HOME_PAGE_LOCATORS['all_add_to_cart_btn']
    cart_btn_locator_type = cart_btns['type']
    cart_btn_locator = cart_btns['locator']

    all_cart_btns = driver_functions.find_elements(context, cart_btn_locator_type, cart_btn_locator)
    random_btns = random.sample(all_cart_btns, int(qty))

    for i in random_btns:
        driver_functions.click(i)
    time.sleep(1)
    # import pdb;pdb.set_trace()

@step("I click on cart in the top nav bar and verify cart page opens")
def i_click_on_cart_in_the_top_nav_bar_and_verify_cart_page_opens(context):
    cart_page_btn = HOME_PAGE_LOCATORS['cart_info_box']
    cart_page_locator_type = cart_page_btn['type']
    cart_page_locator = cart_page_btn['locator']

    driver_functions.click(context, cart_page_locator_type, cart_page_locator)

    driver_functions.assert_url_contains(context, '/cart/')





