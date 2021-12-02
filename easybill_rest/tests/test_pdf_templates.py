import unittest
from unittest import mock

from easybill_rest import Client
from easybill_rest.resources.resource_pdf_templates import ResourcePdfTemplates
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestResourcePdfTemplates(
        unittest.TestCase,
        EasybillRestTestCaseAbstract):

    def setUp(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value={})
        self.mocked_object = ResourcePdfTemplates(mocked_object)

    def test_get_endpoint(self) -> None:
        self.assertEqual(
            "/pdf-templates",
            Client('').pdf_templates().get_resource_endpoint())

    def test_get_pdf_templates(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.get_pdf_templates({"page": "2"}), dict))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestResourcePdfTemplates, [
            'test_get_endpoint',
            'test_get_pdf_templates',
        ]))
