from base.base_driver import BasePage, BaseHandles
from base.find_element import FindElement

'''
po模式页面封装三层架构
'''
'''对象层'''
class HomePage(BasePage):

    # 初始化管理父类方法
    def __init__(self):
        super().__init__()

    # 定位首页登录位置
    def home_login(self):
        return self.find_wait_element(FindElement.login)

    # 假如进入首页已经登录了定位安全退出位置
    def home_anquan(self):
        return self.find_wait_element(FindElement.login_tuichu)

    # 定位用户名输入框
    def home_user(self):
        return self.find_wait_element(FindElement.login_username)

    # 定位密码输入框
    def home_pwd(self):
        return self.find_wait_element(FindElement.login_password)

    # 定位登录按钮
    def home_button(self):
        return self.find_wait_element(FindElement.login_button)

    # 定位鼠标移动位置
    def home_yidong(self):
        return self.find_element(FindElement.home_page_header)

    # 定位用户名信息
    def home_text(self):
        return self.find_wait_element(FindElement.home_page_name)

    # 定位搜索输入框
    def home_sousuo(self):
        return self.find_wait_element(FindElement.home_page_sousuo)

    # 定位搜索按钮
    def home_sousuo_button(self):
        return self.find_wait_element(FindElement.home_page_button)

    # 定位购物车
    def home_card(self):
        return self.find_wait_element(FindElement.home_page_card)


'''
操作层
操作方法
'''
class HomeHandles(BaseHandles):

    # 初始化管理对象层
    def __init__(self):
        self.home_page = HomePage()

    # 登录功能
    def handle_login(self,username,password):
        try:
            # 进去首页如果已登陆，点击安全退出
            self.find_move_to(self.home_page.driver,self.home_page.home_yidong())
            self.find_click(self.home_page.home_anquan())
        except:
            print("用户还没登录请先登录")

        # 点击登录
        self.find_click(self.home_page.home_login())
        # 用户名输入框
        self.find_send_keys(self.home_page.home_user(),username)
        # 密码输入框
        self.find_send_keys(self.home_page.home_pwd(),password)
        # 点击登录
        self.find_click(self.home_page.home_button())
        # 鼠标移动获取文本
        self.find_move_to(self.home_page.driver,self.home_page.home_yidong())
        # 获取用户名信息断言
        return self.find_text(self.home_page.home_text())

    def handle_name(self):
        pass

    # 搜索功能
    def handle_sousuo(self,text):
        # 搜索输入框
        self.find_send_keys(self.home_page.home_sousuo(),text)
        # 点击搜索按钮
        self.find_click(self.home_page.home_sousuo_button())

    # 购物车功能
    def handle_card(self):
        # 点击购物车图标
        self.find_click(self.home_page.home_card())

'''业务层'''
class HomeBuisser():

    # 初始化管理实例化操作层
    def __init__(self):
        self.home_handles = HomeHandles()

    # 登录功能
    def buisser_login(self,username,password):
        return self.home_handles.handle_login(username,password)

    # 登录后断言
    # def buisser_name(self):
    #     return self.home_handles.handle_name()

    # 搜索功能
    def buisser_sousuo(self,text):
        self.home_handles.handle_sousuo(text)

    # 点击购物车
    def buisser_card(self):
        self.home_handles.handle_card()