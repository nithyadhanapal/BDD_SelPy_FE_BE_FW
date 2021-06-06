# Data Access Object


from BDDCommon.CommonHelpers.dbHelpers import DBHelpers

class OrderDAO(object):

    def __init__(self):
        self.db_helper = DBHelpers()

    def get_order_by_id(self, order_id):
        sql = f"SELECT * FROM local.wp_posts WHERE ID = '{order_id}';"
        return self.db_helper.execute_select(sql)