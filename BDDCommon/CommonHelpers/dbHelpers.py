
import pymysql
from BDDCommon.CommonHelpers.credentialsHelper import CredentialHelper

class DBHelpers(object):

    def __init__(self):
        creds_helper = CredentialHelper()
        creds = creds_helper.get_db_credentials()
        self.host = 'localhost'
        self.db_user = creds['db_user']
        self.db_password = creds['db_password']
        self.socket = '/Users/nithya/Library/Application Support/Local/run/BQgW4ALNV/mysql/mysqld.sock'

    def create_db_connection(self):
        self.connection = pymysql.connect(host=self.host, user=self.db_user, password=self.db_password, unix_socket=self.socket)

    def execute_select(self, sql):
        try:
            self.create_db_connection()
            cur = self.connection.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception("Failed running sql {}. Error {}".format(sql, str(e)))
        finally:
            self.connection.close()
        return rs_dict

    def execute_sql(self):
        pass