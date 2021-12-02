import unittest
from unittest import mock

from easybill_rest import Client
from easybill_rest.resources.resource_customer_groups import ResourceCustomerGroups
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestResourceCustomerGroups(
        unittest.TestCase,
        EasybillRestTestCaseAbstract):

    def setUp(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value={})
        self.mocked_object = ResourceCustomerGroups(mocked_object)

    def test_get_endpoint(self) -> None:
        self.assertEqual(
            "/customer-groups",
            Client('').customer_groups().get_resource_endpoint())

    def test_get_customer_groups(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.get_customer_groups({"page": "2"}), dict))

    def test_get_customer_group(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.get_customer_group("3"),
                dict))

    def test_create_customer_group(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.create_customer_group({"test": "test"}), dict))

    def test_update_customer_group(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.update_customer_group(
                    "3", {
                        "test": "test"}), dict))

    def test_delete_customer_group(self) -> None:
        self.assertIsNone(self.mocked_object.delete_customer_group("3"))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestResourceCustomerGroups, [
            'test_get_endpoint',
            'test_get_customer_groups',
            'test_get_customer_group',
            'test_create_customer_group',
            'test_update_customer_group',
            'test_delete_customer_group',
        ]))
