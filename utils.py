import json
import os

from selenium import webdriver

'''
封装常用工具类
webdriver驱动
关闭驱动
数据驱动
'''

class BaseDriver:

    __driver = None

    __open_key = True

    @classmethod
    def open_driver(cls):
        '''
        创建webdriver驱动，打开网站 最大化
        :return:
        '''
        if cls.__driver is None:
            # 打开驱动
            cls.__driver = webdriver.Chrome()
            # 网页最大化
            cls.__driver.maximize_window()
            # 显示等待
            cls.__driver.implicitly_wait(10)
        return cls.__driver

    def open_key(self,key):
        '''
        开关模式
        :param key:
        :return:
        '''
        self.__open_key = key

    @classmethod
    def close_driver(cls):
        if cls.__driver is not None and cls.__open_key == True:
            # 关闭驱动
            cls.__driver.quit()
            # __driver改为None
            cls.__driver = None

# 数据驱动
def Base_Data(login_page):
    # 定义空列表
    data_list = []
    # 读取文件
    with open('./data' + os.sep + login_page ,'r',encoding='utf-8') as file:
        # 转化json格式
        data_json = json.load(file)
        # 遍历data_json字典的值
        for iteam in data_json.values():
            data_list.append(list(iteam.values()))
    # 返回列表数据
    return data_list
