'''
封装鼠标操作事件
'''
from selenium.webdriver import ActionChains

from utils import BaseDriver


class ActionsChains:

    def __init__(self):
        self.driver = BaseDriver.open_driver()

    def action_chains(self):
        '''
        初始化ActionChains
        :return:
        '''
        return ActionChains(self.driver)

    def action_double_click(self,element):
        '''
        鼠标双击操作
        :param element: 元素
        :return:
        '''
        self.action_chains().double_click(element).perform()

    def action_move_to_element(self,element):
        '''
        鼠标悬停操作
        :param element: 元素
        :return:
        '''
        self.action_chains().move_to_element(element).perform()

    def action_context_click(self,element):
        '''
        鼠标右击操作
        :param element: 元素
        :return:
        '''
        self.action_chains().context_click(element).perform()

    def action_drag_and_drop(self,element1,element2):
        '''
        鼠标拖动操作
        :param element: 元素
        :return:
        '''
        self.action_chains().drag_and_drop(element1,element2).perform()

    def action_drag_and_drop_by_offset(self,element,xoffect=260,yoffect=0):
        '''
        鼠标向左向右移动
        :param element: 元素
        :param xoffect: X坐标
        :param yoffect: Y坐标
        :return:
        '''
        self.action_chains().drag_and_drop_by_offset(element,xoffect,yoffect).perform()

    def action_click_and_hold(self,element):
        '''
        鼠标一直按住操作
        :param element: 元素
        :return:
        '''
        self.action_chains().click_and_hold(element).perform()

    def action_move_by_offset(self,x):
        '''
        鼠标拖动操作
        :param x: 坐标
        :return:
        '''
        self.action_chains().move_by_offset(x,0).perform()

    def action_release(self):
        '''
        放开鼠标
        :return:
        '''
        self.action_chains().release().perform()