# coding:utf-8

import base64
import datetime
import hashlib
import locale
import os
import re
import telnetlib
import time
import urllib
import platform
from urllib.parse import quote

if platform.system() == 'Windows':
    locale.setlocale(locale.LC_CTYPE, 'chinese')

GMT_FORMAT = '%a %b %d %Y %H:%M:%S GMT+0800 (中国标准时间)'


def get_root_path():
    """获取项目根路径"""
    project_name = "12306"
    current_path = os.path.abspath(os.path.dirname(__file__))
    return current_path[:current_path.find(project_name) + len(project_name)]


# 13 位
def timestamp():
    return int(round(time.time() * 1000))


# 10 位
def current_timestamp():
    return int(round(time.time()))


def current_hour():
    return datetime.datetime.now().hour


def current_date():
    return datetime.datetime.now().strftime('%Y-%m-%d')


def current_date_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def check_date(text):
    match = re.compile(r'^\d{4}-\d{1,2}-\d{1,2}$').match(text)
    if match:
        return match.group() is not None
    else:
        return False


def decode_secret_str(code):
    return urllib.parse.unquote(code).replace('\n', '')


def url_encode(text):
    return quote(text, 'utf-8')


def proxy_test(proxy):
    try:
        telnetlib.Telnet(proxy.get('ip'), proxy.get('port'), timeout=1)
        return True
    except BaseException as e:
        print(e)
        return False


def get_gmt_time(text):
    """
    Fri Oct 025 2019 00:00:00 GMT+0800 (中国标准时间)
    Sun Oct 06 2019 00:00:00 GMT+0800 (中国标准时间)
    :param text:
    :return:
    """
    return datetime.datetime.strptime(text, '%Y-%m-%d').strftime(GMT_FORMAT)


def sha256(content=None):
    if content:
        m = hashlib.sha256()
        m.update(b'content')
        return m.hexdigest(), base64.urlsafe_b64encode(m.digest()).decode()
    return ""


def validate_date_str(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def validate_time_str(time_str):
    try:
        datetime.datetime.strptime(time_str, '%H:%M:%S')
        return True
    except ValueError:
        return False


def datetime_str_timestamp(datetime_str):
    d = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(d.timetuple()))


if __name__ == '__main__':
    # print(timestamp())
    # print(get_gmt_time('2019-12-29'))
    # print(url_encode('长沙,CSQ'))
    print(datetime_str_timestamp('2019-12-27 23:59:00'))
    print(current_timestamp())
