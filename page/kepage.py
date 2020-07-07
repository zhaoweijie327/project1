from base.base_driver import BasePage, BaseHandles
from base.find_element import FindElement

'''
po模式页面封装三层架构
'''
'''对象层'''
class KePage(BasePage):

    # 初始化管理父类方法
    def __init__(self):
        super().__init__()

    # 定位课程信息
    def ke_java(self):
        return self.find_wait_element(FindElement.java)

    # 定位购物车按钮
    def ke_gouwu_card(self):
        return self.find_wait_element(FindElement.shopp_card)

    # 定位购物车图片
    def ke_yidong_card(self):
        return self.find_wait_element(FindElement.shopp_card_tupian)

    # 定位文本信息
    def ke_text(self):
        return self.find_wait_element(FindElement.shopp_text)

'''
操作层
操作方法
'''
class KeHandles(BaseHandles):

    # 初始化管理对象层
    def __init__(self):
        self.ke_page = KePage()

    # 添加课程到购物车
    def ke_card(self):
        # 点击课程
        self.find_click(self.ke_page.ke_java())
        try:
            # 页面窗口更换操作
            self.find_window(self.ke_page.driver)
        finally:
            # 添加购物车
            self.find_click(self.ke_page.ke_gouwu_card())
            # 移动到购物车
            self.find_move_to(self.ke_page.driver,self.ke_page.ke_yidong_card())
            # 获取文本信息
            return self.find_text(self.ke_page.ke_text())


'''业务层'''
class KgBuisser:

    # 初始化管理实例化操作层
    def __init__(self):
        self.kg_handles = KeHandles()

    # 选择课程加入购物车
    def buisser_card(self):
        return self.kg_handles.ke_card()
