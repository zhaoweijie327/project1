from base.base_driver import BasePage, BaseHandles
from base.find_element import FindElement

'''
po模式页面封装三层架构
'''
'''对象层'''
class OrderPage(BasePage):

    # 初始化管理父类方法
    def __init__(self):
        super().__init__()

    # 定位购物车页面信息
    def order_text(self):
        return self.find_wait_element(FindElement.gouwuche_text)

    # 定位结算按钮
    def order_jiesuan(self):
        return self.find_wait_element(FindElement.gouwuche_jiesuan)

    # 定位提交按钮
    def order_tijiao(self):
        return self.find_wait_element(FindElement.gouwuche_tijiao)

    # 定位订单信息
    def order_dingdan_text(self):
        return self.find_wait_element(FindElement.gouwuche_dingdan_text)

    # 定位立即支付按钮
    def order_zhifu_button(self):
        return self.find_wait_element(FindElement.gouwuche_zhifu)
'''
操作层
操作方法
'''
class OrderHandles(BaseHandles):

    # 初始化管理对象层
    def __init__(self):
        self.order_page = OrderPage()

    # 获取购物车页面信息
    def order_card_text(self):
        # 获取文本信息
        try:
            # 切换窗口
            self.find_window(self.order_page.driver)
        finally:
            return self.find_text(self.order_page.order_text())

    # 结算提交功能
    def order_card(self):
        # 点击结算
        self.find_click(self.order_page.order_jiesuan())
        # 点击提交订单
        self.find_click(self.order_page.order_tijiao())
        # 获取订单信息
        text = self.find_text(self.order_page.order_dingdan_text())
        # 点击立即支付
        self.find_click(self.order_page.order_zhifu_button())
        return text

'''业务层'''
class OrderBuisser:

    # 初始化管理实例化操作层
    def __init__(self):
        self.order_handles = OrderHandles()

    # 获取购物车页面信息
    def order_card_text(self):
        # 获取文本信息
        return self.order_handles.order_card_text()

    # 结算提交功能
    def order_card(self):
        # 结算提交功能
        return self.order_handles.order_card()