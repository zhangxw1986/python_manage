#! /usr/bin/env python
# -*- coding:utf-8 -*-

import functools
import inspect


def check_is_admin(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        func_args = inspect.getcallargs(f, *args, **kwargs)
        if func_args.get('username') != 'admin':
            raise Exception('this user is not allowed get/put element.')
        return f(*args, **kwargs)
    return wrapper


class Stack(object):
    def __init__(self):
        self.storage = []

    @check_is_admin
    def put(self, username, ele):
        self.storage.append(ele)
        print('now stack is', self.storage)

    @check_is_admin
    def get(self, username):
        if not self.storage:
            raise Exception('there is no item in stack')
        self.storage.pop()
        print('now stack is', self.storage)


if __name__ == "__main__":
    s = Stack()
    try:
        s.put('admin', 1)
        s.put("admin", 2)
        s.get('admin')
        s.get('zxw')
        s.put("admin", 3)
    except Exception as e:
        print(e)
        
    