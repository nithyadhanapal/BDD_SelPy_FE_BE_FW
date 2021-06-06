import time

from behave import given, when, then
from BDDCommon.CommonConfigs.locatorConfigs import ORDER_RECEIVED_LOCATORS
from BDDCommon.CommonFuncs import driver_functions

@then("Order confirmation page should load with correct data")
def order_confirmation_page_should_load_with_correct_data(context):
    context.execute_steps("""
        then Order confirmation header should load with correct data
        then Thankyou message should load with correct data
        then Verify the order number and label displayed
    """)

@then("Order confirmation header should load with correct data")
def order_confirmation_header_should_load_with_correct_data(context):

    # check the heading text
    order_received_locator = ORDER_RECEIVED_LOCATORS['order_received_title']
    expected_text = 'Order received'
    driver_functions.assert_element_contains_text(context, expected_text, order_received_locator['type'], order_received_locator['locator'])


@then("Thankyou message should load with correct data")
def thankyou_message_should_load_with_correct_data(context):

    thankyou_locator = ORDER_RECEIVED_LOCATORS['thankyou_notice']
    expected_text1 = 'Thank you. Your order has been received.'
    contains = driver_functions.element_contains_text(context, expected_text1, thankyou_locator['type'], thankyou_locator['locator'])
    assert contains, f"Thank you message of order received page does not contain the text '{expected_text1}'."

@then("Verify the order number and label displayed")
def verify_the_order_number_and_label_displayed(context):

    order_detail_locator = ORDER_RECEIVED_LOCATORS['order_details_order']
    element = driver_functions.find_element(context,order_detail_locator['type'], order_detail_locator['locator'])
    order_text = element.text
    order_text_list = order_text.split('\n')
    label = order_text_list[0]
    order_id = order_text_list[1]

    assert label == 'ORDER NUMBER:', f" 'Order received' page the label for order number is not correct. Expected: 'ORDER NUMBER:', Actual:{label} "
    assert order_id.isnumeric(), f"'Order received' page the order is not numeric. Actual: {order_id}"

    context.order_id = order_id

