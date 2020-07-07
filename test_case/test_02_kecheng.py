import logging

import allure
import pytest

from base.find_element import FindElement
from base.page_init import PageInit
from utils import BaseDriver, Base_Data

'''
组织管理测试登录测试用例
'''

class Test_Ke:

    def setup_class(self):
        # 实例化utils.py的工具类
        self.driver = BaseDriver().open_driver()

    @pytest.fixture(autouse=True)
    def open_url(self):
        # 获取网址打开网页
        self.driver.get(FindElement.url)

    def teardown_class(self):
        # 关闭浏览器驱动
        BaseDriver().close_driver()

    @pytest.mark.parametrize("name,message",Base_Data('sousuo.json'))
    @allure.severity(allure.severity_level.NORMAL)
    def test_ke(self,name,message):
        # 调用homepage搜索方法
        PageInit().home_page().buisser_sousuo(name)
        logging.info("搜索成功:%s" % name)
        # 调用kepage 添加购物车方法
        msg = PageInit().ke_page().buisser_card()
        # 获取用户名进行断言
        assert message == msg
        # 存储登录信息到日志
        logging.info('搜索内容和断言结果：%s,%s,' % (name,message))
        logging.info("添加购物车成功:%s" % message)

