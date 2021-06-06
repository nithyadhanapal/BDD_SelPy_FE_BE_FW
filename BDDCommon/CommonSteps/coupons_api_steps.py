from behave import step
from BDDCommon.CommonHelpers.utilitiesHelper import generate_random_coupon_code
from BDDCommon.CommonAPI import coupons_api
from BDDCommon.CommonDAO.couponsDAO import CouponsDAO

@step("I create a '{discount_type}' coupon")
def create_a_coupon_with_given_discount_type(context, discount_type):
    data = {
        "code": generate_random_coupon_code(),
    }
    if discount_type.lower() != 'none':
        context.expected_discount_type = discount_type
        data["discount_type"] = discount_type
    else:
        context.expected_discount_type = 'fixed_cart'

    rs_api = coupons_api.create_coupon(data)
    context.new_coupon_info = rs_api

@step("The coupon should exist in database")
def the_coupon_should_exist_in_database(context):
    coupon_dao =  CouponsDAO()
    coupon_id = context.new_coupon_info['id']
    db_coupon = coupon_dao.get_coupon_by_id(coupon_id)
    assert db_coupon, f"Coupon not found in database. Coupon id: {coupon_id}"

    coupon_meta = coupon_dao.get_coupon_metadata_by_id(coupon_id)
    assert coupon_meta['discount_type'] == context.expected_discount_type, f"Unexpected 'discount_type' for new coupon. " \
                                                  f"Expected: {context.expected_discount_type}, Actual: {coupon_meta['discount_type']}"

    # import pdb; pdb.set_trace()
