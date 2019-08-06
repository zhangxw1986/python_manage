# -*- coding:utf-8 -*-
import re

def nonCompile(exp,file):
    '''
    re 不提前编译
    '''
    with open(file) as f:
        for line in f:
            re.findall(exp,line)

if __name__ == "__main__":
    exp = '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'  
    file = '/mnt/hgfs/shared_files/python_manage/chap_3/access_log-20190707'
    nonCompile(exp,file)

