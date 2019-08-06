#! /usr/bin/env python
# -*- coding:utf-8 -*-


def times(length=1):
    def bread(f):
        def wrapper(*args, **kwargs):
            for i in range(length):
                f(*args, **kwargs)
        return wrapper
    return bread


@times(5)
def say_hi():
    print('hello world')


if __name__ == "__main__":
    say_hi()
