# Data Access Object
import logging as logger

from BDDCommon.CommonHelpers.dbHelpers import DBHelpers

class CouponsDAO(object):

    def __init__(self):
        self.db_helper = DBHelpers()

    def get_coupon_by_id(self, coupon_id):
        sql = f"SELECT * FROM local.wp_posts WHERE ID = {coupon_id} AND post_type = 'shop_coupon';"
        return self.db_helper.execute_select(sql)

    def get_coupon_metadata_by_id(self, coupon_id):
        sql = f"SELECT * FROM local.wp_postmeta WHERE post_id = '{coupon_id}';"
        rs_sql = self.db_helper.execute_select(sql)
        logger.debug(f"SQL result: \n {rs_sql}")

        coupon_meta = dict()
        for i in rs_sql:
            coupon_meta[i['meta_key']] = i['meta_value']
        return coupon_meta