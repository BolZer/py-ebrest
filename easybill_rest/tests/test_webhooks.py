import unittest
from unittest import mock

from easybill_rest import Client
from easybill_rest.resources.resource_webhooks import ResourceWebhooks
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestResourceWebhooks(unittest.TestCase, EasybillRestTestCaseAbstract):

    def setUp(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value={})
        self.mocked_object = ResourceWebhooks(mocked_object)

    def test_get_endpoint(self) -> None:
        self.assertEqual("/webhooks", Client('').webhooks().get_resource_endpoint())

    def test_get_webhooks(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.get_webhooks({"page": "2"}), dict))

    def test_get_webhook(self) -> None:
        self.assertTrue(isinstance(self.mocked_object.get_webhook("3"), dict))

    def test_create_webhooks(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.create_webhook({"test": "test"}), dict))

    def test_update_webhook(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.update_webhook(
                    "3", {
                        "test": "test"}), dict))

    def test_delete_webhook(self) -> None:
        self.assertIsNone(self.mocked_object.delete_webhook("3"))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestResourceWebhooks, [
            'test_get_endpoint',
            'test_get_webhooks',
            'test_get_webhook',
            'test_create_webhooks',
            'test_update_webhook',
            'test_delete_webhook'
        ]))
