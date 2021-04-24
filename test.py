# -*- coding: utf-8 -*
from urllib import request
import re
import time
import zmail
import Log

log = Log.MyLog()

mail_content = {
    'subject': '可以抢票了！',
    'content_text': '可以抢票了！This message from zmail!'
}

server = zmail.server('501278040@qq.com', 'trhgetpudruebhih')
#
if server.smtp_able():
    pass
if server.pop_able():
    pass


def findLeft(day):
    result0 = re.search(day, output)
    if result0:
        day = '<b>' + day + '</b>'
        result = re.search("(%s*)已售罄(%s*)" % (day, '</li>'), output, re.S)
        if result:
            log.info("已售罄"+day)
            pass
        else:
            log.info('mail'+day)
            server.send_mail('better941218@163.com', mail_content)
    else:
        log.error("no day")
        pass


if __name__ == '__main__':
    i = 0
    while True:
        with request.urlopen('https://gugong.ktmtech.cn/') as html:
            data = html.read()
            output = data.decode('utf-8', 'ignore')
            # print(output)
        findLeft('5月4日')
        findLeft('5月2日')
        findLeft('5月5日')
        i=i+1
        log.info("已循环%s次"%i)
        time.sleep(5)