import unittest
from unittest import mock

from easybill_rest import Client
from easybill_rest.resources.resource_tasks import ResourceTasks
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestResourceTasks(unittest.TestCase, EasybillRestTestCaseAbstract):

    def setUp(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value={})
        self.mocked_object = ResourceTasks(mocked_object)

    def test_get_endpoint(self) -> None:
        self.assertEqual("/tasks", Client('').tasks().get_resource_endpoint())

    def test_get_tasks(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.get_tasks({"page": "2"}), dict))

    def test_get_task(self) -> None:
        self.assertTrue(isinstance(self.mocked_object.get_task("3"), dict))

    def test_create_task(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.create_task({"sale_price": "2000"}), dict))

    def test_update_task(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.update_task(
                    "3", {
                        "sale_price": "2500"}), dict))

    def test_delete_task(self) -> None:
        self.assertIsNone(self.mocked_object.delete_task("3"))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestResourceTasks, [
            'test_get_endpoint',
            'test_get_tasks',
            'test_get_task',
            'test_create_task',
            'test_update_task',
            'test_delete_task',
        ]))
