from BDDCommon.CommonHelpers.wooRequestHelpers import WooRequestHelper

def create_user(data):

    return WooRequestHelper().post(wc_endpoint='customers', params=data, expected_status_code=201)
