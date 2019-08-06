#!/usr/bin/env python3                     #标准注释，保证.py文件可在unix系统上运行
# -*- coding: utf-8  -*-                   #标准注释，表示.py文件都用标准UTF-8编码
#  'a test module'                            # 模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

import os
import fnmatch

def is_file_match(filename,patterns):
    for pattern in patterns:
        print("ok")