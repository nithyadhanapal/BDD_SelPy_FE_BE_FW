from BDDCommon.CommonHelpers.wooRequestHelpers import WooRequestHelper

def create_coupon(data):
    return WooRequestHelper().post('coupons', data, expected_status_code=201)
