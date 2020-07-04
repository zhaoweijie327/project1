'''管理定位元素'''
from selenium.webdriver.common.by import By


class FindElement:

    # ------------网址------------
    url = "https://www.imooc.com/"

    # ------------首页------------
    login = (By.CSS_SELECTOR,'#js-signin-btn') # 点击首页登录按钮
    login_username = (By.CSS_SELECTOR,'.xa-emailOrPhone') # 输入用户名
    login_password = (By.CSS_SELECTOR,'.js-pass-pwd') # 输入密码
    login_button = (By.CSS_SELECTOR,'.xa-login') # 点击登录
    home_page_header = (By.CSS_SELECTOR,'#header-avator') # 鼠标移动某位置操作
    home_page_name = (By.CSS_SELECTOR,'.text-ellipsis') # 获取用户名信息
    home_page_sousuo = (By.CSS_SELECTOR,'.search-input') # 搜索框输入内容
    home_page_button = (By.CSS_SELECTOR,'.icon-search') # 点击搜索
    home_page_card = (By.CSS_SELECTOR,'.shop-cart-icon') # 点击购物车

    # ------------课程列表页面------------
    java = (By.CSS_SELECTOR,'[data-type="战课程"]') # 点击课程

    # ------------课程详情页面------------
    shopp_card = (By.LINK_TEXT,'加入购物车') # 点击加入购物车
    shopp_card_tupian = (By.CSS_SELECTOR,'.imv2-shopping-cart2') # 鼠标移动操作
    shopp_text = (By.CSS_SELECTOR,'.content-box h3') # 获取购物车产品信息

    # ------------购物车页面------------
    gouwuche_text = (By.CSS_SELECTOR,'.cart-title h1') # 获取购物车页面信息
    gouwuche_jiesuan = (By.CSS_SELECTOR,'.li-3 .js-go-confrim') # 点击去结算
    gouwuche_tijiao = (By.LINK_TEXT,'提交订单') # 点击提交订单
    gouwuche_dingdan_text = (By.CSS_SELECTOR,'.order') # 获取订单信息
    gouwuche_zhifu = (By.CSS_SELECTOR,'.pay-summary-submit') # 点击立即支付