import logging

import allure
import pytest

from base.find_element import FindElement
from base.page_init import PageInit
from utils import BaseDriver, Base_Data

'''
组织管理测试登录测试用例
'''

class Test_Order:

    def setup_class(self):
        # 实例化utils.py的工具类
        self.driver = BaseDriver().open_driver()

    @pytest.fixture(autouse=True)
    def open_url(self):
        # 获取网址打开网页
        self.driver.get(FindElement.url)

    def teardown_class(self):
        # 关闭浏览器驱动
        BaseDriver.open_key(True)
        BaseDriver().close_driver()

    @pytest.mark.parametrize("card,dingdan",Base_Data('jiesuan_tijiao.json'))
    @allure.severity(allure.severity_level.NORMAL)
    def test_order(self,card,dingdan):
        # 调用homepage点击购物车方法
        PageInit().home_page().buisser_card()
        # 调用orderpage 获取购物侧页面信息方法
        msg = PageInit().order_page().order_card_text()
        # 获取购物车页面信息进行断言
        assert card == msg
        # 调用orderpage 结算方法
        text = PageInit().order_page().order_card()
        assert dingdan == text
        logging.info('断言结果：%s,%s,' % (card,dingdan))
        logging.info("提交成功" )