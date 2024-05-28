import unittest
from unittest import mock

from easybill_rest import Client
from easybill_rest.resources.resource_documents import ResourceDocuments, SendMethod
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestResourceDocuments(unittest.TestCase, EasybillRestTestCaseAbstract):

    def setUp(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value={})
        self.mocked_object = ResourceDocuments(mocked_object)

    def test_get_endpoint(self) -> None:
        self.assertEqual("/documents", Client('').documents().get_resource_endpoint())

    def test_get_documents(self) -> None:
        self.assertTrue(isinstance(self.mocked_object.get_documents(), dict))

    def test_get_document(self) -> None:
        self.assertTrue(isinstance(self.mocked_object.get_document("3"), dict))

    def test_create_document(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.create_document({"title": "test"}), dict))

    def test_update_document(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.update_document(
                    "3", {
                        "title": "test"}), dict))

    def test_delete_document(self) -> None:
        self.assertIsNone(self.mocked_object.delete_document("3"))

    def test_finalize_document(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.finalize_document("3"),
                dict))

    def test_cancel_document(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.cancel_document("3"),
                dict))

    def test_send_document(self) -> None:
        self.assertIsNone(
            self.mocked_object.send_document(
                "3", SendMethod.EMAIL, {}))

    def test_download_document_as_pdf(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.download = mock.Mock(return_value=bytes('test', 'utf-8'))
        self.assertTrue(
            isinstance(
                ResourceDocuments(mocked_object).download_document_as_pdf("3"),
                bytes))

    def test_download_document_as_jpeg(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.download = mock.Mock(return_value=bytes('test', 'utf-8'))
        self.assertTrue(
            isinstance(
                ResourceDocuments(mocked_object).download_document_as_jpeg("3"),
                bytes))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestResourceDocuments, [
            'test_get_endpoint',
            'test_get_documents',
            'test_get_document',
            'test_create_document',
            'test_update_document',
            'test_delete_document',
            'test_finalize_document',
            'test_cancel_document',
            'test_send_document',
            'test_download_document_as_pdf',
            'test_download_document_as_jpeg'
        ]))
