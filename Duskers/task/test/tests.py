from typing import List

import utils.helper.useful
from utils import from_stage4_tests, global_tests

from hstest import StageTest, TestCase
from hstest.dynamic.input.dynamic_testing import search_dynamic_tests


class Test(StageTest):
    def generate(self) -> List[TestCase]:
        utils.helper.useful.StageData.STAGE_NO = 4
        return (search_dynamic_tests(global_tests.GlobalDuskersTest)
                + search_dynamic_tests(from_stage4_tests.FromStage4DuskersTest))
