import logging
import os
import time


LEVELS = {
    'debug': logging.DEBUG,
    'info' : logging.INFO,
    'warning' : logging.WARNING,
    'error' : logging.ERROR,
    'critical' : logging.CRITICAL
}

logger = logging.getLogger()
level = 'default'

def create_file(file_name):
    path = file_name[0:file_name.rfind('/')]#字符串切片，rfind方法返回最后一个/的下标；
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(file_name):
        f = open(file_name, mode= 'w', encoding='utf-8')
        f.close()

def set_handler(levels):
    # 给logger添加handler
    if levels == 'error':
        logger.addHandler(MyLog.err_handler)
        # logger.addHandler(MyLog.streamHandler)
    logger.addHandler(MyLog.handler)
    # logger.addHandler(MyLog.streamHandler)

def remove_handler(levels):
    if levels == 'error':
        logger.removeHandler(MyLog.err_handler)
        # logger.removeHandler(MyLog.streamHandler)
    logger.removeHandler(MyLog.handler)
    # logger.removeHandler(MyLog.streamHandler)

def get_current_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

class MyLog:
    path = os.path.abspath(os.path.dirname(__file__))
    # print(path)
    log_file = path+'/Log/default.log'
    err_file = path+'/Log/error.log'
    # 创建logger
    logger.setLevel(LEVELS.get(level,logging.NOTSET))
    create_file(log_file)
    create_file(err_file)
    #创建两个个handler，分别用于写入default和error日志文件
    handler = logging.FileHandler(log_file, encoding='utf-8')
    err_handler = logging.FileHandler(err_file, encoding='utf-8')
    # 再创建一个handler，用于输出到控制台
    # streamHandler = logging.StreamHandler()

    @staticmethod
    def debug(log_meg):
        set_handler('debug')
        logger.debug("【DEBUG】" + get_current_time() + log_meg)
        remove_handler('debug')
    @staticmethod
    def info(log_meg):
        set_handler('info')
        logger.debug("【INFO】" + get_current_time() + log_meg)
        remove_handler('info')
    @staticmethod
    def warning(log_meg):
        set_handler('warning')
        logger.debug("【WARNING】" + get_current_time() + log_meg)
        remove_handler('warning')
    @staticmethod
    def error(log_meg):
        set_handler('error')
        logger.debug("【ERROR】" + get_current_time() + log_meg)
        remove_handler('error')
    @staticmethod
    def critical(log_meg):
        set_handler('critical')
        logger.debug("【CRITICAL】" + get_current_time() + log_meg)
        remove_handler('critical')

if __name__ == '__main__':
    MyLog.debug('debug测试')
    MyLog.error('测试')