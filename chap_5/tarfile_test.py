#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import tarfile

def open_tar():
    
    with tarfile.open('tarfile_test.tar') as t:
        for member in t.getmembers():
            print(member.name)

def add_tar():
     with tarfile.open('tarfile_test.tar',mode='w') as t:
         t.add('out.txt')

if __name__ == "__main__":
    # add_tar()
    open_tar()









