from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from utils import BaseDriver


'''封装driver的基类'''

class BasePage:

    # 初始化utils的open_driver方法
    def __init__(self):
        self.driver = BaseDriver.open_driver()

    # 封装单个元素定位方法
    def find_element(self,loc):
        '''
        # 封装单个元素定位方法
        :param loc:
        :return:
        '''
        element = self.driver.find_element(*loc)
        return element


    def find_elements(self, loc):
        '''
        # 封装一组元素定位方法
        :param loc: 元素
        :return:
        '''
        elements = self.driver.find_elements(*loc)
        return elements

    # 封装显示等待单个元素定位方法
    def find_wait_element(self, loc,waittime=10,sousuotime=1.0):
        '''
        显示等待单个元素方法
        :param loc: 元素
        :param waittime:
        :param sousuotime:
        :return:
        '''
        element = WebDriverWait(self.driver,waittime,sousuotime).until(lambda x : x.find_element(*loc))
        return element


    def find_wait_elements(self, loc,waittime=10,sousuotime=1.0):
        '''
        # 封装显示等待一组元素定位方法
        :param loc:  元素
        :param waittime:
        :param sousuotime:
        :return:
        '''
        elements = WebDriverWait(self.driver,waittime,sousuotime).until(lambda x : x.find_elements(*loc))
        return elements

'''封装基本操作方法'''
class BaseHandles:

    def find_send_keys(self,element,text):
        '''
        # 输入方法
        :param element: 元素
        :param text: 输入内容
        :return:
        '''
        element.clear()
        element.send_keys(text)

    def find_click(self,element):
        '''
        # 点击方法
        :param element: 元素
        :return:
        '''
        element.click()

    def find_text(self,element):
        '''
        # 获取文本信息
        :param element: 元素
        :return:
        '''
        return element.text

    def find_get_attribute(self,element):
        '''
        获取链接/图片路径
        :param element:元素
        :return:
        '''
        return element.get_attribute()

    def find_is_displayed(self,element):
        '''
        判断元素是否可见方法
        :param element: 元素
        :return:
        '''
        return element.is_displayed()

    def find_is_enabled(self,element):
        '''
        元素是否可用
        :return:
        '''
        return element.is_enabled()

    def find_is_selected(self,element):
        '''
        检查复选框或单选框是否被选中
        :param element: 元素
        :return:
        '''
        return element.is_selected()

    def find_back(self,driver):
        '''
        # 后退操作
        :param driver: 驱动对象
        :return:
        '''
        driver.back()

    def find_forward(self,driver):
        '''
        前进操作
        :return:
        '''
        driver.forward()

    def find_refresh(self,driver):
        '''
        刷新操作
        :return:
        '''
        driver.refresh()

    def find_window(self,driver):
        '''
        # 切换窗口操作
        :param driver: 驱动对象
        :return:
        '''
        lists = driver.window_handles  # 获取所有窗口句柄 返回的是列表　第一步
        driver.switch_to.window(lists[-1])  # 切换指定的句柄 用下标找 -1 从后头切换　第二步

    def find_frame(self,driver,element,tag=1):
        '''
        # 切换子页面
        :param driver: 驱动对象
        :param element: 元素
        :param tag: 默认值为1
        :return:
        '''
        if tag == 1:
            # 进入子页面
            driver.switch_to.frame(element)
        else:
            # 退出主页面
            driver.switch_to.default_content()

    def find_alert(self,driver,tag=1):
        '''
        # 弹窗操作
        :param driver: 驱动对象
        :param tag: 默认值为1
        :return:
        '''
        # 获取弹出框对象
        alert = driver.switch_to.alert
        if tag == 1:
            # 点击确定按钮
            alert.accept()
        elif tag == 2:
            # 点击取消
            alert.dismiss()
        else:
            # 获取弹出框信息
            return alert.text

    def find_select(self, element, tag=1, index=0, values=None, text=None):
        '''
        下拉列表方法
        :param element: 元素
        :param tag: 默认为1
        :param index: 下表默认0
        :param values: 默认空
        :param text: 默认空
        :return:
        '''
        select = Select(element)
        if tag == 1:
            # 表示所有的option列表里面的属性值 下标控制
            select.select_by_index(index)
        if tag == 2:
            # 选择下拉列表里面的元素
            select.deselect_by_value(values)
        else:
            # 获取文本打印属性值信息
            return select.select_by_visible_text(text)

    def find_js(self,driver):
        '''
        利用js方法把滚动条拖动到底部
        :param driver: 驱动对象
        :return:
        '''
        js = 'window.scrollTo(0,1000000)'
        driver.execute_script(js)

    def find_key(self,element,tag=1):
        '''
        键盘操作
        :param element:
        :param tag: 默认1
        :return:
        '''
        if tag == 1:
            # 删除键操作 .send_keys(Keys.BACK_SPACE)
            element.send_keys(Keys.BACK_SPACE)
        elif tag == 2:
            # 空格键操作 .send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
        elif tag == 3:
            # 回退操作 .send_keys(Keys.CANCEL)
            element.send_keys(Keys.CANCEL)
        elif tag == 4:
            # 全选操作 .send_keys(Keys.CONTROL,'a')
            element.send_keys(Keys.CONTROL, 'a')
        elif tag == 5:
            # 复制操作 .send_keys(Keys.CONTROL,'c')
            element.send_keys(Keys.CONTROL, 'c')
        else:
            # 粘贴操作 .send_keys(Keys.CONTROL,'v')
            element.send_keys(Keys.CONTROL, 'v')


