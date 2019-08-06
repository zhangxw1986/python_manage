#!/usr/bin/env python3                     #标准注释，保证.py文件可在unix系统上运行
# -*- coding: utf-8  -*-                   #标准注释，表示.py文件都用标准UTF-8编码
#  'a test module'                            # 模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

import os
from collections import Counter



def main():
    c = Counter()
    with open(os.path.expanduser('~/.bash_history')) as f:
        for line in f:
            cmd = line.strip().split()
            if cmd:
                c[cmd[0]] += 1
    print(c.most_common(10))

if __name__ == "__main__":
    main()

        