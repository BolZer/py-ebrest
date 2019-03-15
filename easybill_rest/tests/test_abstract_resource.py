import unittest

from easybill_rest.resources.resource_abstract import ResourceAbstract
from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestAbstractResource(unittest.TestCase, EasybillRestTestCaseAbstract):

    def test_abstract_method(self):
        abstract_class = ResourceAbstract()
        self.assertTrue(hasattr(abstract_class, '_abc_impl'))

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestAbstractResource, [
            'test_abstract_method',
        ]))
