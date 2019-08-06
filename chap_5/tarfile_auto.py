#! /usr/bin/env python
# -*- coding:utf-8 -*-

import fnmatch
import os,sys
import tarfile

def is_file_match(filename,patterns):
    for pattern in patterns:
        if fnmatch.fnmatch(filename,pattern):
            return True
    return False

def find_special_files(path,patterns=["*"],ex_dir=[]):
    for root,dirnames,files in os.walk(path):
        for file in files:
            if is_file_match(file,patterns):
                yield os.path.join(root,file)
        for d in ex_dir:
            dirnames.remove(d)

def show_tar():
    with tarfile.open('tarfile.tar.gz',mode='r:gz') as t:
        for member in t.getmembers():
            print(member.name)

def add_tar(path,patterns,ex_dir):
     with tarfile.open('tarfile.tar.gz',mode='w:gz') as t:
         for file in find_special_files(path,patterns,ex_dir):
             t.add(file)


def main():
    path='/mnt/hgfs/shared_files/python_manage/chap_5'
    patterns = ["*.jpg","*.txt"]
    ex_dir=[]
    add_tar(path,patterns,ex_dir)

if __name__ == "__main__":
    # main()
    show_tar()



    
