from behave import given, when, then
from BDDCommon.CommonConfigs.locatorConfigs import ORDER_RECEIVED_LOCATORS
from BDDCommon.CommonFuncs import driver_functions
from BDDCommon.CommonDAO.orderDAO import OrderDAO

@then("I verify order is created in database")
def i_verify_order_is_created_in_database(context):

    db_order = OrderDAO().get_order_by_id(context.order_id)

    assert db_order, f"Order id {context.order_id} is not found in database"
    assert db_order[0]['post_type'] == 'shop_order', f"For order id '{context.order_id}', the 'post_type field' " \
                                                     f"value is not as expected. Actual: '{db_order[0]['post_type']}'"
