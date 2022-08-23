# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨（caituotuo.top）
# 时间：2022/5/21 20:45
# 功能：测试用例

import allure
import pytest

from utils.get_logger import GetLogger
from utils.get_time import GetTime
from api.daxue import DaXue


class TestCaseDaXue:
    time = GetTime().get_now_datetime()
    logger = GetLogger().get_logger()

    def setup(self):
        self.logger.info(self.time + " >>>>>> 开始执行：")

    def teardown(self):
        self.logger.info(self.time + " >>>>>> 执行结束！")

    @allure.title("真实大学——四川轻化工大学")
    def test1(self):
        DaXue().daxue("data/req.yml")

    # @allure.title("真实大学——厦门大学")
    # def test2(self):
    #     DaXue().daxue("data/req2.yml")

    # @allure.title("不存在的大学")
    # def test3(self):
    #     DaXue().daxue("data/req3.yml")


if __name__ == '__main__':
    pytest.main()
