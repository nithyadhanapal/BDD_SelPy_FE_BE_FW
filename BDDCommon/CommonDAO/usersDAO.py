# Data Access Object


from BDDCommon.CommonHelpers.dbHelpers import DBHelpers

class UsersDAO(object):

    def __init__(self):
        self.db_helper = DBHelpers()

    def get_user_by_email(self, email):
        sql = f"SELECT * FROM local.wp_users WHERE user_email = '{email}';"
        return self.db_helper.execute_select(sql)