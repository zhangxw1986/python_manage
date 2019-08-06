# -*- coding:utf-8 -*-

import functools

import sys
from os.path import dirname,abspath
path = dirname(dirname(abspath(__file__)))
print(path)
sys.path.append(path)

from chap_5.find_file import *


'abc'

__author__ = 'zhangxiangwu'
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call {0}()'.format(func.__name__))
        return func(*args,**kw)
    return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('{0} call {1}()'.format(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2019-6-14')

if __name__ == "__main__":
    now()
    patt = ['*.py']
    is_file_match('def_decorator.py',patt)
    print('__name__: {0}'.format(__name__))
    print('__author__: {0}'.format(__author__))
    print('__doc__: {0}'.format(__doc__))