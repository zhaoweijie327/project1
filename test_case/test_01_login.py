import logging

import pytest

from base.find_element import FindElement
from base.page_init import PageInit
from utils import BaseDriver, Base_Data

'''
组织管理测试登录测试用例
'''

class Test_Login:

    def setup_class(self):
        # 实例化utils.py的工具类
        self.driver = BaseDriver().open_driver()

    def setup(self):
        # 获取网址打开网页
        self.driver.get(FindElement.url)

    def teardown_class(self):
        # 关闭浏览器驱动
        BaseDriver().close_driver()

    @pytest.mark.parametrize("username,password,message",Base_Data('login_page.json'))
    def test_login(self,username,password,message):
        # 调用homepage登录的业务方法
        msg = PageInit().home_page().buisser_login(username,password)
        # 获取用户名进行断言
        assert message == msg
        # 存储登录信息到日志
        logging.info('登录信息：%s,%s,%s' % (username,password,message))
        logging.info("登录成功")

