from selenium.webdriver.support.wait import WebDriverWait

from utils import BaseDriver


'''封装driver的基类'''

class BasePage():

    # 初始化utils的open_driver方法
    def __init__(self):
        self.driver = BaseDriver.open_driver()

    # 封装单个元素定位方法
    def find_element(self,loc):
        element = self.driver.find_element(*loc)
        return element

    # 封装单个元素定位方法
    def find_elements(self, loc):
        elements = self.driver.find_elements(*loc)
        return elements

    # 封装显示等待单个元素定位方法
    def find_wait_element(self, loc,waittime=10,sousuotime=1.0):
        element = WebDriverWait(self.driver,waittime,sousuotime).until(lambda x : x.find_element(*loc))
        return element

    # 封装显示等待单个元素定位方法
    def find_wait_elements(self, loc,waittime=10,sousuotime=1.0):
        elements = WebDriverWait(self.driver,waittime,sousuotime).until(lambda x : x.find_elements(*loc))
        return elements

'''封装基本操作方法'''
class BaseHandles():

    # 封装输入方法
    def find_send_keys(self,element,text):
        element.send_keys(text)

    # 封装输入方法
    def find_click(self,element):
        element.click()

    # 封装输入方法
    def find_text(self,element):
        return element.text