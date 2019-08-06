#!/usr/bin/env python
# -*- coding:utf-8 -*-

import codecs
from contextlib import contextmanager


class Open(object):
    def __init__(self, file, mode, encoding='utf-8'):
        self.fp = codecs.open(file, mode, encoding)

    def __enter__(self):
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()


@contextmanager
def Oopen(file, mode, encoding='utf-8'):
    fp = codecs.open(file, mode, encoding)
    try:
        yield fp
    finally:
        fp.close()


if __name__ == "__main__":
    data = '我是中国人'
    with Open('data.txt', 'w') as f:
        f.write(data)

    with Oopen('odata.txt', 'w') as f1:
        f1.write(data)
