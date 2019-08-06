#! /usr/bin/env python
# -*- coding:utf-8 -*-


def bread(f):
    
    def wrapper(*args,**kwargs):
        print("begin")
        f(*args,**kwargs)
        print("end")
        # return f(*args,**kwargs)

    return wrapper

@bread
def say_hi(a=1):
    print('hello world',a)
    
if __name__ == "__main__":
    say_hi()