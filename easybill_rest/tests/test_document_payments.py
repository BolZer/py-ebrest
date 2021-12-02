import unittest
from unittest import mock

from easybill_rest import Client
from easybill_rest.resources.resource_document_payments import ResourceDocumentPayments
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestResourceDocumentPayments(
        unittest.TestCase,
        EasybillRestTestCaseAbstract):

    def setUp(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value={})
        self.mocked_object = ResourceDocumentPayments(mocked_object)

    def test_get_endpoint(self) -> None:
        self.assertEqual("/document-payments",
                         Client('').document_payments().get_resource_endpoint())

    def test_get_document_payments(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.get_document_payments({"page": "2"}), dict))

    def test_get_document_payment(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.get_document_payment("3"),
                dict))

    def test_create_document_payment(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.create_document_payment({"test": "test"}), dict))

    def test_delete_document_payment(self) -> None:
        self.assertIsNone(self.mocked_object.delete_document_payment("3"))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestResourceDocumentPayments, [
            'test_get_endpoint',
            'test_get_document_payments',
            'test_get_document_payment',
            'test_create_document_payment',
            'test_delete_document_payment',
        ]))
