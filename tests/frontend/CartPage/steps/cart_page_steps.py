import time
from behave import given, when, then
from BDDCommon.CommonConfigs.locatorConfigs import CART_PAGE_LOCATORS
from BDDCommon.CommonFuncs import driver_functions

@when("I click on 'Proceed to checkout' button in the cart page")
def i_click_on_proceed_to_checkout_button_in_the_cart_page(context):
    checkout_btn = CART_PAGE_LOCATORS['proceed_to_checkout_btn']
    checkout_btn_locator_type = checkout_btn['type']
    checkout_btn_locator = checkout_btn['locator']

    driver_functions.click(context, checkout_btn_locator_type, checkout_btn_locator)

    driver_functions.assert_url_contains(context, '/checkout/')

@when("I get the total amount of the cart")
def i_get_the_total_amount_of_the_cart(context):
    time.sleep(2)
    total_amount_locator = CART_PAGE_LOCATORS['total_cart_value']
    total_amt_text = driver_functions.get_element_text(context, total_amount_locator['type'], total_amount_locator['locator'])
    context.total_amount = total_amt_text.replace('$','')


@when("I get a valid {pct}% off coupon")
def i_get_a_valid_pct_off_coupon(context, pct):

    if int(pct) == 50:
        context.coupon_code = 'TEST50'
    else:
        raise Exception("Not implemented")


@when("I apply coupon on the cart")
def i_apply_coupon_on_the_cart(context):
    coupon_code_locator = CART_PAGE_LOCATORS['coupon_code']
    apply_code_locator = CART_PAGE_LOCATORS['apply_coupon']
    coupon_applied_msg_locator = CART_PAGE_LOCATORS['coupon_applied_msg']
    driver_functions.type_into_element(context, context.coupon_code, coupon_code_locator['type'], coupon_code_locator['locator'])
    driver_functions.click(context, apply_code_locator['type'], apply_code_locator['locator'])

    expected_message = 'Coupon code applied successfully.'
    driver_functions.assert_element_contains_text(context, expected_message,
                                            coupon_applied_msg_locator['type'], coupon_applied_msg_locator['locator'])



@then("The total should be reduced by {pct}%")
def the_total_should_be_reduced_by_pct(context, pct):

    original_total_amount =  context.total_amount
    expected_new_total = float(original_total_amount) * (float(pct) / 100)
    context.execute_steps("when I get the total amount of the cart")
    new_total = context.total_amount
    assert expected_new_total == float(new_total), f"Cart total after applying {pct}% coupon is not as expected." \
                                                   f"Original total: {original_total_amount}, " \
                                                   f"Expected total: {expected_new_total}, "  \
                                                   f"Actual total: {new_total}"

