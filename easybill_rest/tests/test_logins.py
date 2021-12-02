import unittest
from unittest import mock

from easybill_rest import Client
from easybill_rest.resources.resource_logins import ResourceLogins
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestResourceLogins(unittest.TestCase, EasybillRestTestCaseAbstract):

    def setUp(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value={})
        self.mocked_object = ResourceLogins(mocked_object)

    def test_get_endpoint(self) -> None:
        self.assertEqual("/logins", Client('').logins().get_resource_endpoint())

    def test_get_logins(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.get_logins({"page": "2"}), dict))

    def test_get_login(self) -> None:
        self.assertTrue(isinstance(self.mocked_object.get_login("3"), dict))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestResourceLogins, [
            'test_get_endpoint',
            'test_get_logins',
            'test_get_login',
        ]))
