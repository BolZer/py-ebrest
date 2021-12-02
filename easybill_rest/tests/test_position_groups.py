import unittest
from unittest import mock

from easybill_rest import Client
from easybill_rest.resources.resource_position_groups import ResourcePositionGroups
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestResourcePositionGroups(
        unittest.TestCase,
        EasybillRestTestCaseAbstract):

    def setUp(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value={})
        self.mocked_object = ResourcePositionGroups(mocked_object)

    def test_get_endpoint(self) -> None:
        self.assertEqual(
            "/position-groups",
            Client('').position_groups().get_resource_endpoint())

    def test_get_position_groups(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.get_position_groups({"page": "2"}), dict))

    def test_get_position_group(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.get_position_group("3"),
                dict))

    def test_create_position_group(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.create_position_group({"test": "test"}), dict))

    def test_update_position_group(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.update_position_group(
                    "3", {
                        "test": "test"}), dict))

    def test_delete_position_group(self) -> None:
        self.assertIsNone(self.mocked_object.delete_position_group("3"))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestResourcePositionGroups, [
            'test_get_endpoint',
            'test_get_position_groups',
            'test_get_position_group',
            'test_create_position_group',
            'test_update_position_group',
            'test_delete_position_group',
        ]))
