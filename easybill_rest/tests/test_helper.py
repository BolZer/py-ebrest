import unittest

from easybill_rest.helper import Helper
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestHelper(unittest.TestCase, EasybillRestTestCaseAbstract):

    def test_create_request_url_from_params_with_payload(self):
        result = Helper.create_request_url_from_params("/test", {"id": 23})
        self.assertTrue(True if result.find("/rest/v1/") > -1 else False)
        self.assertTrue(True if result.find("23") > -1 else False)
        self.assertTrue(True if result.find("/test") > -1 else False)

    def test_create_request_url_from_params_without_payload(self):
        result = Helper.create_request_url_from_params("/test")
        self.assertTrue(True if result.find("/rest/v1/test") > -1 else False)
        self.assertTrue(True if result.find("23") == -1 else False)

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestHelper, [
            'test_create_request_url_from_params_with_payload',
            'test_create_request_url_from_params_without_payload',
        ]))
