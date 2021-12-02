import unittest
from unittest import mock

from easybill_rest import Client
from easybill_rest.resources.resource_contacts import ResourceContacts
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestResourceContacts(unittest.TestCase, EasybillRestTestCaseAbstract):

    def setUp(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value={})
        self.mocked_object = ResourceContacts(mocked_object)

    def test_get_endpoint(self) -> None:
        self.assertEqual("/customers", Client('').contacts().get_resource_endpoint())

    def test_get_contacts(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.get_contacts(
                    "2", {
                        "page": "2"}), dict))

    def test_get_contact(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.get_contact(
                    "2", "3"), dict))

    def test_create_contact(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.create_contact(
                    "2", {
                        "test": "test"}), dict))

    def test_update_contact(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.update_contact(
                    "1", "3", {
                        "test": "test"}), dict))

    def test_delete_contact(self) -> None:
        self.assertIsNone(self.mocked_object.delete_contact("1", "3"))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestResourceContacts, [
            'test_get_endpoint',
            'test_get_contacts',
            'test_get_contact',
            'test_create_contact',
            'test_update_contact',
            'test_delete_contact',
        ]))
