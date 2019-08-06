#! /usr/bin/env python
# -*- coding:utf-8 -*-

import time
import threading


def say_hi(name):
    time.sleep(2)
    print('hello world,{0}'.format(name))


def main():
    '''
    线程无并发和有并发的对比
    '''
    # 以下是无线程并发
    # for i in range(5):
    #     say_hi()

    # 有线程并发
    li = ['bob','steve','avi','kkk','env']
    for i in range(5):
        thread = threading.Thread(target=say_hi,args=(li[i],))
        thread.start()


if __name__ == "__main__":
    main()
