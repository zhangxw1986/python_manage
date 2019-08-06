#!/usr/bin/env python3                     #标准注释，保证.py文件可在unix系统上运行
# -*- coding: utf-8  -*-                   #标准注释，表示.py文件都用标准UTF-8编码
#  'a test module'                            # 模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

import os

print('current directory is : ',os.getcwd())
path = os.path.abspath(__file__)
print('full path of current file is :' ,path)
print('parent directory of current file : ' ,os.path.abspath(os.path.join(os.path.dirname(path),os.path.pardir)))