from page.homepage import HomeBuisser
from page.kepage import KgBuisser
from page.orderpage import OrderBuisser

'''
管理业务层实例化方法
'''

class PageInit:

    @classmethod
    def home_page(cls):
        '''首页'''
        return HomeBuisser()

    @classmethod
    def ke_page(cls):
        '''课程列表'''
        return KgBuisser()

    @classmethod
    def order_page(cls):
        '''结算提交订单'''
        return OrderBuisser()