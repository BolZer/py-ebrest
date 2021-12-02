import unittest
from unittest import mock

from easybill_rest import Client
from easybill_rest.resources.resource_attachments import ResourceAttachments
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestResourceAttachments(unittest.TestCase, EasybillRestTestCaseAbstract):

    def setUp(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value={})
        mocked_object.upload = mock.Mock(return_value={})
        mocked_object.download = mock.Mock(return_value=bytes())
        self.mocked_object = ResourceAttachments(mocked_object)

    def test_get_endpoint(self) -> None:
        self.assertEqual("/attachments", Client('').attachments().get_resource_endpoint())

    def test_get_attachments(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.get_attachments({"page": "2"}), dict))

    def test_get_attachment(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.get_attachment("3"),
                dict))

    def test_create_attachment(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.create_attachment(
                    bytes(
                        '{"test": "test"}',
                        'utf-8')),
                dict))

    def test_update_attachment(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.update_attachment(
                    "3", {
                        "test": "test"}), dict))

    def test_delete_attachment(self) -> None:
        self.assertIsNone(self.mocked_object.delete_attachment("3"))

    def test_get_content(self) -> None:
        self.assertIsNotNone(self.mocked_object.get_content("3"))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestResourceAttachments, [
            'test_get_endpoint',
            'test_get_attachments',
            'test_get_attachment',
            'test_create_attachment',
            'test_update_attachment',
            'test_delete_attachment',
            'test_get_content',
        ]))
