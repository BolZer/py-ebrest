import unittest
from unittest import mock

from easybill_rest import Client
from easybill_rest.resources.resource_document_versions import ResourceDocumentVersions
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestResourceDocumentVersions(unittest.TestCase, EasybillRestTestCaseAbstract):

    def setUp(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value={})
        self.mocked_object = ResourceDocumentVersions(mocked_object)

    def test_get_endpoint(self) -> None:
        self.assertEqual("/documents", Client('').document_versions().get_resource_endpoint())

    def test_get_document_versions(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.get_document_version(
                    "1", "1",), dict))

    def test_get_document_version(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.get_document_versions(
                    "1", {
                        "page": "2"}), dict))

    def test_download_document_version_item(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.download = mock.Mock(return_value=bytes('test', 'utf-8'))
        self.assertTrue(
            isinstance(
                ResourceDocumentVersions(mocked_object).download_document_version_item(
                    "1",
                    "1",
                    "1",
                ), bytes))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestResourceDocumentVersions, [
            'test_get_endpoint',
            'test_get_document_versions',
            'test_get_document_version',
            'test_download_document_version_item'
        ]))
