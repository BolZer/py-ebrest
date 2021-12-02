import unittest
from unittest import mock

from easybill_rest import Client
from easybill_rest.resources.resource_post_boxes import ResourcePostBoxes
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestResourcePostBoxes(unittest.TestCase, EasybillRestTestCaseAbstract):

    def setUp(self) -> None:
        mocked_object = mock.Mock()
        mocked_object.call = mock.Mock(return_value={})
        self.mocked_object = ResourcePostBoxes(mocked_object)

    def test_get_endpoint(self) -> None:
        self.assertEqual("/post-boxes", Client('').post_boxes().get_resource_endpoint())

    def test_get_post_boxes(self) -> None:
        self.assertTrue(isinstance(
            self.mocked_object.get_post_boxes({"page": "2"}), dict))

    def test_get_post_box(self) -> None:
        self.assertTrue(isinstance(self.mocked_object.get_post_box("3"), dict))

    def test_delete_post_box(self) -> None:
        self.assertIsNone(self.mocked_object.delete_post_box("3"))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestResourcePostBoxes, [
            'test_get_endpoint',
            'test_get_post_boxes',
            'test_get_post_box',
            'test_delete_post_box',
        ]))
