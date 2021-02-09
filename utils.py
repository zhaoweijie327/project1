import json
import os

from selenium import webdriver

'''
封装常用工具类
webdriver驱动
关闭驱动
数据驱动
'''
# 绝对路径
BAS_URL = os.path.abspath(os.path.dirname(__file__))

class BaseDriver:

    __driver = None

    __open_key = True

    @classmethod
    def open_driver(cls,brower='chrome'):
        '''
        创建webdriver驱动，打开网站 最大化
        :return:
        '''

        if cls.__driver is None:
            if brower == 'chrome':
                # 打开谷歌驱动
                cls.__driver = webdriver.Chrome()
            elif brower == 'firefox':
                # 打开火狐驱动
                cls.__driver = webdriver.Firefox()
            else:
                # 打开IE驱动
                cls.__driver = webdriver.Ie()
            # 网页最大化
            cls.__driver.maximize_window()
            # 显示等待
            cls.__driver.implicitly_wait(10)
        return cls.__driver

    @classmethod
    def open_key(cls,key):
        '''
        开关模式
        :param key:
        :return:
        '''
        cls.__open_key = key

    @classmethod
    def close_driver(cls):
        if cls.__driver is not None and cls.__open_key == True:
            # 关闭驱动
            cls.__driver.quit()
            # __driver改为None
            cls.__driver = None


# 数据驱动
class DataDriven:

    def data_driver(self,folder='/data'):
        # 读取文件
        with open(BAS_URL + folder ,'r',encoding='utf-8') as file:
            # 转化json格式
            data_json = json.load(file)
            return data_json

    def create_dict(self,path=None):
        '''
        通过字典形式获取   {
                                "xxx":{

                                            }
                                }
        :return:
        '''
        # 创建列表
        data_dict = []
        # 获取json数据
        data = self.data_driver(path)
        for i in data.values():
            # 把值保存到列表
            data_dict.append(list(i.values()))
        # 返回列表
        return data_dict

    def create_list(self,path=None):
        '''
                通过字典形式获取   [
                                          {
                                            "xxx": "xxx",
                                            "xxx": {
                                              "xxx": "xxx",
                                            }
                                        ]
                :return:
                '''
        # 创建列表
        data_list = []
        # 获取json数据
        data = self.data_driver(path)
        for i in data:
            # 把值保存到列表
            data_list.append(list(i.values()))
        # 返回列表
        return data_list

    def create_values(self,values,path=None):
        '''
                获取单个键里面的值   {
                                "xxx":{

                                            }
                                }
                :return:
                '''
        data_list = []
        # 获取json数据
        data = self.data_driver(path)
        # 获取值
        data_values = data.get(values)
        # 值保存在列表
        data_list.append(list(data_values.values()))
        # 返回列表
        return data_list