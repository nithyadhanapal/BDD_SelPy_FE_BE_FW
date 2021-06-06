from behave import step
from BDDCommon.CommonFuncs import driver_functions
from BDDCommon.CommonConfigs.locatorConfigs import MY_ACCOUNT_LOCATORS

@step("I type '{username}' into the username of login form")
def type_username_into_username_of_login_form(context, username):
    """
    :param context:
    :param username:
    :return:
    """
    username_locator_type = MY_ACCOUNT_LOCATORS['login_user_name']['type']
    username_locator = MY_ACCOUNT_LOCATORS['login_user_name']['locator']
    driver_functions.type_into_element(context, username, username_locator_type,username_locator)


@step("I type '{password}' into the password of login form")
def type_password_of_the_login_form(context, password):
    """

    :param context:
    :param password:
    :return:
    """
    password_locator_type = MY_ACCOUNT_LOCATORS['login_password']['type']
    password_locator = MY_ACCOUNT_LOCATORS['login_password']['locator']
    driver_functions.type_into_element(context,password,password_locator_type,password_locator)

@step("I click on '{btn_name}' button")
def click_on_login_button(context,btn_name):
    """

    :param context:
    :return:
    """
    if btn_name.lower() in ("login","log in"):
        login_button_locator_type = MY_ACCOUNT_LOCATORS['login_btn']['type']
        login_button_locator = MY_ACCOUNT_LOCATORS['login_btn']['locator']
    else:
        raise Exception ("Not Implemented")
    driver_functions.click(context,login_button_locator_type,login_button_locator)

@step("User should be logged in")
def User_should_be_logged_in(context):

    nav_bar_locator_type = MY_ACCOUNT_LOCATORS['left_nav_bar']['type']
    nav_bar_locator = MY_ACCOUNT_LOCATORS['left_nav_bar']['locator']

    logout_button_locator_type = MY_ACCOUNT_LOCATORS['left_nav_logout_btn']['type']
    logout_button_locator = MY_ACCOUNT_LOCATORS['left_nav_logout_btn']['locator']

    driver_functions.assert_element_visible(context,nav_bar_locator_type,nav_bar_locator)
    driver_functions.assert_element_visible(context,logout_button_locator_type,logout_button_locator)

@step("error message with username '{username}' should be displayed")
def error_message_with_username_should_be_displayed(context, username):

    error_box_locator_type = MY_ACCOUNT_LOCATORS['error_box']['type']
    error_box_locator = MY_ACCOUNT_LOCATORS['error_box']['locator']
    expected_message = "Error: The password you entered for the username {} is incorrect. Lost your password?".format(username)
    is_exist = driver_functions.element_contains_text(context,expected_message, error_box_locator_type, error_box_locator)

    if is_exist:
        print("Correct error message is displayed for failed login")
        print("111")
    else:
        raise Exception("Correct error message is not displayed for failed login:{}".format(username))

@step("error message with 'Unknown username' should be displayed")
def error_message_with_unknown_username_should_be_displayed(context):

    error_box_locator_type = MY_ACCOUNT_LOCATORS['error_box']['type']
    error_box_locator = MY_ACCOUNT_LOCATORS['error_box']['locator']
    expected_message = "Unknown username. Check again or try your email address."
    is_exist = driver_functions.element_contains_text(context,expected_message, error_box_locator_type, error_box_locator)

    if is_exist:
        print("Correct error message is displayed for non-existing username")
        print("111")
    else:
        raise Exception("Correct error message is not displayed for non-existing username")