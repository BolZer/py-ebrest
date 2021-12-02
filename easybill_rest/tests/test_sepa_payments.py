import unittest
from unittest import mock

from easybill_rest import Client
from easybill_rest.resources.resource_sepa_payments import ResourceSepaPayments
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestResourceSepaPayments(
        unittest.TestCase,
        EasybillRestTestCaseAbstract):

    def setUp(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value={})
        self.mocked_object = ResourceSepaPayments(mocked_object)

    def test_get_endpoint(self) -> None:
        self.assertEqual(
            "/sepa-payments",
            Client('').sepa_payments().get_resource_endpoint())

    def test_get_sepa_payments(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.get_sepa_payments({"page": "2"}), dict))

    def test_get_sepa_payment(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.get_sepa_payment("3"),
                dict))

    def test_create_sepa_payments(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.create_sepa_payment({"test": "test"}), dict))

    def test_update_sepa_paymemnt(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.update_sepa_payment(
                    "3", {
                        "sale_price": "2500"}), dict))

    def test_delete_sepa_payment(self) -> None:
        self.assertIsNone(self.mocked_object.delete_sepa_payment("3"))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestResourceSepaPayments, [
            'test_get_endpoint',
            'test_get_sepa_payments',
            'test_get_sepa_payment',
            'test_create_sepa_payments',
            'test_update_sepa_paymemnt',
            'test_delete_sepa_payment',
        ]))
