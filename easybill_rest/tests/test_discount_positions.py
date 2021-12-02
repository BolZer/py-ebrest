import unittest
from unittest import mock

from easybill_rest import Client
from easybill_rest.resources.resource_discount_positions import ResourceDiscountPositions
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestResourceDiscountPositions(
        unittest.TestCase,
        EasybillRestTestCaseAbstract):

    def setUp(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value={})
        self.mocked_object = ResourceDiscountPositions(mocked_object)

    def test_get_endpoint(self) -> None:
        self.assertEqual("/discounts/position",
                         Client('').discount_positions().get_resource_endpoint())

    def test_get_position_discounts(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.get_position_discounts({"page": "2"}), dict))

    def test_get_position_discount(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.get_position_discount("3"),
                dict))

    def test_create_position_discount(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.create_position_discount({"test": "test"}), dict))

    def test_update_position_discount(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.update_position_discount(
                    "3", {
                        "test": "test"}), dict))

    def test_delete_position_discount(self) -> None:
        self.assertIsNone(self.mocked_object.delete_position_discount("3"))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestResourceDiscountPositions, [
            'test_get_endpoint',
            'test_get_position_discounts',
            'test_get_position_discount',
            'test_create_position_discount',
            'test_update_position_discount',
            'test_delete_position_discount',
        ]))
