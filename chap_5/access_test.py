#!/usr/bin/env python3                     #标准注释，保证.py文件可在unix系统上运行
# -*- coding: utf-8  -*-                   #标准注释，表示.py文件都用标准UTF-8编码
#  'a test module'                            # 模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

import os
import sys

def main():
    sys.argv.append("")
    print(sys.argv)
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        raise SystemExit(filename + ' does not exists.')
    elif not os.access(filename,os.R_OK):
        os.chmod(filename,777)
    else:
        with open(filename) as f:
            print(f.read())

if __name__ == "__main__":
    main()