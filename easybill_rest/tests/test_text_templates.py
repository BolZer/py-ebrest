import unittest
from unittest import mock

from easybill_rest import Client
from easybill_rest.resources.resource_text_templates import ResourceTextTemplates
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestResourceTextTemplates(
        unittest.TestCase,
        EasybillRestTestCaseAbstract):

    def setUp(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value={})
        self.mocked_object = ResourceTextTemplates(mocked_object)

    def test_get_endpoint(self) -> None:
        self.assertEqual(
            "/text-templates",
            Client('').text_templates().get_resource_endpoint())

    def test_get_text_templates(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.get_text_templates({"page": "2"}), dict))

    def test_get_text_template(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.get_text_template("3"),
                dict))

    def test_create_text_template(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.create_text_template({"test": "test"}), dict))

    def test_update_text_template(self) -> None:
        self.assertTrue(
            isinstance(
                self.mocked_object.update_text_template(
                    "3", {
                        "test": "test"}), dict))

    def test_delete_text_template(self) -> None:
        self.assertIsNone(self.mocked_object.delete_text_template("3"))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestResourceTextTemplates, [
            'test_get_endpoint',
            'test_get_text_templates',
            'test_get_text_template',
            'test_create_text_template',
            'test_update_text_template',
            'test_delete_text_template',
        ]))
