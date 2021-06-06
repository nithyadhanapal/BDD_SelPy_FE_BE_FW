from BDDCommon.CommonHelpers.wooRequestHelpers import WooRequestHelper

def list_of_products():
    """

    :return:
    """
    all_products = []
    max_pages = 1000
    page_number = 1
    while page_number < max_pages:
        param = {'per_page' : 100, 'page': page_number} # If param is not defined, only 10 rows per page will be fetched
        rs_api = WooRequestHelper().get(wc_endpoint='products', params = param)
        print("Page numbers: {}".format(page_number))
        if rs_api:
            page_number += 1
            all_products.extend(rs_api)
        else:
            print("No results on page number {}. End loop of calling products".format(page_number))
            break

    return all_products

def get_product_by_id(product_id):
    """

    :param product_id:
    :return:
    """
    rs_api = WooRequestHelper().get(wc_endpoint="products/{}".format(product_id))

    return rs_api