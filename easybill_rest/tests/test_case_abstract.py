from __future__ import annotations

import unittest
from abc import ABC


class EasybillRestTestCaseAbstract(ABC):

    @staticmethod
    def get_suite() -> unittest.TestSuite:
        raise NotImplementedError
