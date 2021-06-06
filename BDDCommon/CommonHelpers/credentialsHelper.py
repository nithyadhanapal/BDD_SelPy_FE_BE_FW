"""
To set the environmet variables in a separate class instead of hard coding.
Go to termianl _> Venv -> type env -> to the environment variables set
"""

import os

class CredentialHelper(object):

    def __init__(self):
        pass

    def get_wc_api_credentials(self):
        wc_key = os.environ.get('WC_KEY')
        wc_secret = os.environ.get('WC_SECRET')

        if not wc_key or not wc_secret:
            raise Exception("The credentials for API 'WC_KEY' and 'WC_SECRET' must be set as env variables.")
        else:
            return {'WC_KEY':wc_key, 'WC_SECRET': wc_secret}

    def get_db_credentials(self):
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')

        if not db_user or not db_password:
            raise Exception("The credentials for Database 'DB_USER' and 'DB_PASSWORD' must be set as env variables.")
        else:
            return {'db_user': db_user, 'db_password': db_password}

if __name__ == '__main__':
    obj = CredentialHelper()
    print(obj.get_wc_api_credentials())

# (venv_bdd_pro2_py3) MacBook-Pro-2:BDD_SelPy_FE_BE_FW nithya$ python3 BDDCommon/CommonHelpers/credentialsHelper.py
# {'WC_KEY': 'ck_5a379ae21c4664e775e427e8008ea2a61643b574', 'WC_SECRET': 'cs_71629768676ab90f9eed5d04e3bf8dbf601e0bb9'}
