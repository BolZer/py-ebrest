import unittest
from unittest import mock

from easybill_rest import Client
from easybill_rest.resources.resource_discount_position_groups import ResourceDiscountPositionGroups
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestResourceDiscountPositionGroups(
        unittest.TestCase,
        EasybillRestTestCaseAbstract):

    def setUp(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value={})
        self.mocked_object = ResourceDiscountPositionGroups(mocked_object)

    def test_get_endpoint(self) -> None:
        self.assertEqual("/discounts/position-group",
                         Client('').discount_position_groups()._endpoint)

    def test_get_position_group_discounts(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.get_position_group_discounts({"page": "2"}), dict))

    def test_get_position_group_discount(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.get_position_group_discount("3"),
                dict))

    def test_create_position_group_discount(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.create_position_group_discount({"test": "test"}), dict))

    def test_update_position_group_discount(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.update_position_group_discount(
                    "3", {
                        "test": "test"}), dict))

    def test_delete_position_group_discount(self) -> None:
        self.assertIsNone(
            self.mocked_object.delete_position_group_discount("3"))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestResourceDiscountPositionGroups, [
            'test_get_endpoint',
            'test_get_position_group_discounts',
            'test_get_position_group_discount',
            'test_create_position_group_discount',
            'test_update_position_group_discount',
            'test_delete_position_group_discount',
        ]))
