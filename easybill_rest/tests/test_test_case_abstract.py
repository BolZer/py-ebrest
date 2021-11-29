import unittest

from easybill_rest.tests.test_case_abstract import EasybillRestTestCaseAbstract


class TestEaybillTestCaseAbstract(
        unittest.TestCase,
        EasybillRestTestCaseAbstract):

    def test_test_case_abstract(self) -> None:
        self.assertRaises(
            NotImplementedError,
            EasybillRestTestCaseAbstract.get_suite)

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        return unittest.TestSuite(map(TestEaybillTestCaseAbstract, [
            'test_test_case_abstract',
        ]))
