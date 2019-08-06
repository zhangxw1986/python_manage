#!/usr/bin/env python3                     #标准注释，保证.py文件可在unix系统上运行
# -*- coding: utf-8  -*-                   #标准注释，表示.py文件都用标准UTF-8编码
#  'a test module'                            # 模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释
__author__ = 'zxw'                     #作者名
import sys
import os                                 #        导入模块
import fileinput

for line in fileinput.input():
    meta = [fileinput.filename(),fileinput.fileno(),fileinput.isfirstline()]
    print(*meta,end=" ")
    print(line,end=" ")
