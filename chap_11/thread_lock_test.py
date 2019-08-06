#! /usr/bin/env python
# -*- coding:utf-8 -*-

import threading


lock = threading.Lock()
num = 0


def incre(count):
    global num
    with lock:
        while count > 0:
            num += 1
            count -= 1


def main():
    threads = []
    for i in range(10):
        thread = threading.Thread(target=incre, args=(100000,))
        thread.start()
        threads.append(thread)

    for td in threads:
        td.join()

    print('expect value is ', 10*100000, '.  real num is ', num)


if __name__ == "__main__":
    main()
