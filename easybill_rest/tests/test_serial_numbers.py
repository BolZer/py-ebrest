import unittest
from unittest import mock

from easybill_rest import Client
from easybill_rest.resources.resource_serial_numbers import ResourceSerialNumbers
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestResourceSerialNumbers(
        unittest.TestCase,
        EasybillRestTestCaseAbstract):

    def setUp(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value={})
        self.mocked_object = ResourceSerialNumbers(mocked_object)

    def test_get_endpoint(self) -> None:
        self.assertEqual(
            "/serial-numbers",
            Client('').serial_numbers().get_resource_endpoint())

    def test_get_serial_numbers(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.get_serial_numbers({"page": "2"}), dict))

    def test_get_serial_number(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.get_serial_number("3"),
                dict))

    def test_create_serial_number(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.create_serial_number({"serial": "2000"}), dict))

    def test_delete_serial_number(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value=None)
        self.mocked_object = ResourceSerialNumbers(mocked_object)
        self.assertIsNone(self.mocked_object.delete_serial_number("3"))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestResourceSerialNumbers, [
            'test_get_endpoint',
            'test_get_serial_numbers',
            'test_get_serial_number',
            'test_create_serial_number',
            'test_delete_serial_number',
        ]))
