# LOCATORS = {
#     'main navigation' : {'type': 'id', 'locator':'mainnav'},
#     'top navigation' : {'type': 'id', 'locator':'top'},
#     'options' : {'type': 'css selector', 'locator':'.options-bar'}
# }

MY_ACCOUNT_LOCATORS = {
    'login_user_name' : {'type': 'id', 'locator':'username'},
    'login_password' : {'type': 'id', 'locator':'password'},
    'login_btn' : {'type': 'css selector', 'locator':'button[name="login"]'},
    'left_nav_bar' : {'type': 'class name', 'locator':'woocommerce-MyAccount-navigation'},
    'left_nav_logout_btn' : {'type': 'css selector', 'locator':'div.entry-content nav.woocommerce-MyAccount-navigation ul li:nth-of-type(6)'},
    'error_box' : {'type': 'css selector', 'locator':'ul.woocommerce-error'},
}

HOME_PAGE_LOCATORS = {
    'all_add_to_cart_btn' : {'type': 'css selector', 'locator': 'li.product a.ajax_add_to_cart'},
    'cart_info_box' : {'type': 'css selector', 'locator': "ul.site-header-cart"},
}

CART_PAGE_LOCATORS = {
    'proceed_to_checkout_btn' : {'type': 'css selector', 'locator': "div.wc-proceed-to-checkout"},
    'total_cart_value' : {'type': 'css selector', 'locator': "tr.order-total span.woocommerce-Price-amount"},
    'coupon_code' : {'type': 'id', 'locator': "coupon_code"},
    'apply_coupon': {'type': 'name', 'locator': "apply_coupon"},
    'coupon_applied_msg' : {'type': 'css selector', 'locator': 'div.woocommerce-message'}

}

CHECKOUT_PAGE_LOCATORS = {
    'checkout_title': {'type': 'css selector', 'locator': "header.entry-header h1.entry-title"},
    'checkout_form': {'type': 'xpath', 'locator': "//form[@name='checkout']"},
    'first_name' : {'type': 'id', 'locator': "billing_first_name"},
    'last_name' : {'type': 'id', 'locator': "billing_last_name"},
    'country' : {'type': 'id', 'locator': "billing_last_name"},
    'address' : {'type': 'id', 'locator': "billing_address_1"},
    'city' : {'type': 'id', 'locator': "billing_city"},
    'state' : {'type': 'id', 'locator': "billing_city"},
    'zip_code' : {'type': 'name', 'locator': "billing_postcode"},
    'phone_number' : {'type': 'id', 'locator': "billing_phone"},
    'email' : {'type': 'id', 'locator': "billing_email"},
    'place_order_btn' : {'type': 'id', 'locator': "place_order"},
}

ORDER_RECEIVED_LOCATORS = {
    'order_received_title': {'type': 'css selector', 'locator': "header.entry-header h1.entry-title"},
    'thankyou_notice': {'type': 'css selector', 'locator': "div.woocommerce-order p.woocommerce-thankyou-order-received"},
    'order_details_order': {'type': 'css selector', 'locator': "ul.order_details li.order"},
    'order_details_date': {'type': 'css selector', 'locator': "ul.order_details li.date"},
    'order_details_total': {'type': 'css selector', 'locator': "ul.order_details li.total"},
    'order_details_method': {'type': 'css selector', 'locator': "ul.order_details li.method"},
}