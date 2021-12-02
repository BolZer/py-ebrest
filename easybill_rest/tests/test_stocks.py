import unittest
from unittest import mock

from easybill_rest import Client
from easybill_rest.resources.resource_stocks import ResourceStocks
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestResourceStocks(unittest.TestCase, EasybillRestTestCaseAbstract):

    def setUp(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value={})
        self.mocked_object = ResourceStocks(mocked_object)

    def test_get_endpoint(self) -> None:
        self.assertEqual("/stocks", Client('').stocks().get_resource_endpoint())

    def test_get_stocks(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.get_stocks({"page": "2"}), dict))

    def test_get_stock(self) -> None:
        self.assertTrue(isinstance(self.mocked_object.get_stock("3"), dict))

    def test_create_stock(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.create_stock({"count": "2000"}), dict))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestResourceStocks, [
            'test_get_endpoint',
            'test_get_stocks',
            'test_get_stock',
            'test_create_stock',
        ]))
