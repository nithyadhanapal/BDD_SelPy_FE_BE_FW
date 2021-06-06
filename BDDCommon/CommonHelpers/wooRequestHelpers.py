from woocommerce import API
from BDDCommon.CommonHelpers.credentialsHelper import CredentialHelper
import logging as logger

class WooRequestHelper(object):

    def __init__(self):

        crets_helper = CredentialHelper()
        wc_creds = crets_helper.get_wc_api_credentials()

        self.wcapi = API(
            url="http://localhost:10003",
            consumer_key=wc_creds['WC_KEY'],
            consumer_secret=wc_creds['WC_SECRET'],
            version="wc/v3"
        )

    def assert_status_code(self):
        assert self.rs.status_code == self.expected_status_code, "Bad status code Endpoint: {}, Param: {}." \
        "Actual status code: {}, Expected status code: {}, response_body: {}".format(self.wc_endpoint, self.params, self.rs.status_code,
                                                                  self.expected_status_code, self.rs.json())

    def get(self, wc_endpoint, params=None, expected_status_code=200):
        """"""

        self.rs = self.wcapi.get(wc_endpoint, params=params)
        self.wc_endpoint = wc_endpoint
        self.expected_status_code = expected_status_code
        self.params = params
        # import pdb;pdb.set_trace() # (Pdb) self.rs.status_code #(Pdb) pp self.rs.json()  (Pdb) len(self.rs.json())
        self.assert_status_code()

        return self.rs.json()

    def post(self, wc_endpoint, params=None, expected_status_code=200):
        """

        :param wc_endpoint:
        :param params:
        :param expected_status_code:
        :return:
        """
        logger.info(f"Params: {params}")
        self.rs = self.wcapi.post(wc_endpoint, data=params)
        self.wc_endpoint = wc_endpoint
        self.expected_status_code = expected_status_code
        self.params = params
        # import pdb;pdb.set_trace() # (Pdb) self.rs.status_code #(Pdb) pp self.rs.json()  (Pdb) len(self.rs.json())
        self.assert_status_code()

        return self.rs.json()











if __name__ == '__main__':
    obj = WooRequestHelper()
    # obj.get("products")

    payload = {
            "email" : "dummyemail1@example.com",
            "password" : "test123"
                }

    response = obj.post("customers", params=payload, expected_status_code=201)
    import pprint; pprint.pprint(response)
