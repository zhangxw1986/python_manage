# -*- coding:utf-8 -*-

from collections import Counter
import os
 

def queryPv(filepath):
    '''
    请求pv（总访问量）和uv（不同用户数）
    '''
    li = []
    with open(filepath) as f:
        for line in f:
            client = line.split()[0]
            li.append(client)

    pv = len(li)
    uv = len(set(li))
    return pv,uv

def counterCommon(filepath):
    '''
    最常访问的url，前5排名
    '''
    c = Counter()
    with open(filepath) as f:
        for line in f:
            url = line.split()[6]
            c[url] +=1
    print("popular top access is {0}".format(c.most_common(10))) 

def successRate(filename):
    '''
    统计请求的成功率
    '''
    d = {}
    with open(filename) as f:
        for line in f:
            key =  line.split()[8]
            d.setdefault(key,0)
            d[key] +=1
    sucesscount=0
    failcount=0
    for key,value in d.items():
        if(int(key) > 300):
            failcount += value
        sucesscount += value
    print("success rate is {0:.2f}%".format(sucesscount/(sucesscount+failcount)*100))


if __name__ == "__main__":
    path = '/mnt/hgfs/shared_files/python_manage/chap_3/'
    files = [item for item in os.listdir(path) if item.startswith("access")]
    for file in files:
        pv,uv = queryPv(path+file)
        print("pv is {0}".format(pv))
        print("uv is {0}".format(uv))

        counterCommon(file)
        successRate(file)
        
