import unittest
from unittest import mock

from easybill_rest import Client
from easybill_rest.resources.resource_projects import ResourceProjects
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestResourceProjects(unittest.TestCase, EasybillRestTestCaseAbstract):

    def setUp(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value={})
        self.mocked_object = ResourceProjects(mocked_object)

    def test_get_endpoint(self) -> None:
        self.assertEqual("/projects", Client('').projects().get_resource_endpoint())

    def test_get_projects(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.get_projects({"page": "2"}), dict))

    def test_get_pproject(self) -> None:
        self.assertTrue(isinstance(self.mocked_object.get_project("3"), dict))

    def test_create_project(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.create_project({"sale_price": "2000"}), dict))

    def test_update_project(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.update_project(
                    "3", {
                        "sale_price": "2500"}), dict))

    def test_delete_project(self) -> None:
        self.assertIsNone(self.mocked_object.delete_project("3"))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestResourceProjects, [
            'test_get_endpoint',
            'test_get_projects',
            'test_get_pproject',
            'test_create_project',
            'test_update_project',
            'test_delete_project',
        ]))
