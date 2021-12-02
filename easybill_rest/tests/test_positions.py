import unittest
from unittest import mock

from easybill_rest import Client
from easybill_rest.resources.resource_positions import ResourcePositions
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestResourcePositions(unittest.TestCase, EasybillRestTestCaseAbstract):

    def setUp(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value={})
        self.mocked_object = ResourcePositions(mocked_object)

    def test_get_endpoint(self) -> None:
        self.assertEqual("/positions", Client('').positions().get_resource_endpoint())

    def test_get_positions(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.get_positions({"page": "2"}), dict))

    def test_get_position(self) -> None:
        self.assertTrue(isinstance(self.mocked_object.get_position("3"), dict))

    def test_create_position(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.create_position({"sale_price": "2000"}), dict))

    def test_update_position(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.update_position(
                    "3", {
                        "sale_price": "2500"}), dict))

    def test_delete_position(self) -> None:
        self.assertIsNone(self.mocked_object.delete_position("3"))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestResourcePositions, [
            'test_get_endpoint',
            'test_get_positions',
            'test_get_position',
            'test_create_position',
            'test_update_position',
            'test_delete_position',
        ]))
