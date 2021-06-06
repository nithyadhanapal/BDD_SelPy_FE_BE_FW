from behave import step
from BDDCommon.CommonHelpers.utilitiesHelper import generate_random_email_password
from BDDCommon.CommonAPI import user_api
from BDDCommon.CommonDAO.usersDAO import UsersDAO

@step("I generate random email and password")
def i_generate_random_email_and_password(context):

    random_info = generate_random_email_password()
    context.random_email = random_info['email']
    context.random_password = random_info['password']

@step("I call 'create customer' api")
def i_call_create_customer_api(context):

    payload = {'email': context.random_email, 'password': context.random_password}
    create_user_response = user_api.create_user(data=payload)
    assert create_user_response, "Empty response for create user. Payload: {}".format(payload)
    assert create_user_response['email'] == context.random_email, "Wrong email in response of 'create user' api." \
                    "Call email: {}, response email: {}".format(context.random_email,create_user_response['email'] )

    expected_user_name = context.random_email.split('@')[0]
    assert create_user_response['username'] == expected_user_name, "Wrong 'username' in response of 'create user' api." \
                    "Call username: {}, response username: {}".format(expected_user_name,create_user_response['username'] )

@step("customer should be created")
def customer_should_be_created(context):

    db_user = UsersDAO().get_user_by_email(context.random_email)

    # (Pdb) db_user To find the response and to get assert values
    assert len(db_user) == 1, f"Find user by email found {len(db_user)} results. Emails: {context.random_email}"
    expected_user_name = context.random_email.split('@')[0]
    assert db_user[0]['user_login'] == expected_user_name, f"User created in DB doesnt have the expected user name." \
                                                                   "Expected: {expected_user_name}, " \
                                                                   "Actual: {db_user.split()[0]['user_login']}"

