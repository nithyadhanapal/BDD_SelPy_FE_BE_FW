
from behave import given, when, then, step
from BDDCommon.CommonFuncs import driver_functions
import pdb
# start of step definitions

@step("I go to '{page}' page")
@given('I go to the site "{page}"')
def go_to_page(context, page):
    """
    Step definition to go to the specified url.
    :param context:
    :param url:
    """

    print("Navigating to the page: {}".format(page))
    driver_functions.go_to(context, page)

#========================================================================================#