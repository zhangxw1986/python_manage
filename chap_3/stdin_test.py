# -*- conding:utf-8 -*-

from __future__ import print_function
import sys

try:
    for line in sys.stdin:
        print(line,end="")
except KeyboardInterrupt as e:
    print("now exit")
    exit

