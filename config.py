import logging
import logging.handlers
import os


def logging_rizhi():

    # 创建日志器对象
    rizhiqi = logging.getLogger()
    rizhiqi.setLevel(level=logging.INFO)
    # 创建处理器（按时间切割日志文件）
    lht = logging.handlers.TimedRotatingFileHandler('./log' + os.sep + 'log.log',when='M',interval=1,backupCount=2)
    ls = logging.StreamHandler()
    # 创建格式化器对象
    fmt_name = '%(asctime)s %(levelname)s [%(name)s] ' \
               '[%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt=fmt_name)
    # 给处理器设置格式化器
    lht.setFormatter(formatter)
    # 给日志器添加处理器
    rizhiqi.addHandler(lht)
    rizhiqi.addHandler(ls)