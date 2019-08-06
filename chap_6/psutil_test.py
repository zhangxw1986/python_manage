#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import psutil
import yagmail
import jinja2
import socket
from datetime import datetime


EMAIL_USER = 'stevenzhang1346@163.com'
EMAIL_PASSWORD = 'zz'
RECIPIENTS = ['stevezhang1346@sina.com','zhangxiangwu.zh@ccb.com']


def bytes2num(n):
    symbols = ('K', 'M', 'G', 'T')
    prefix = {}
    for i, s in enumerate(symbols):
        # 1左移多少位
        prefix[s] = 1 << ((i+1)*10)
        # print(prefix[s])
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '{0:.2f}{1}'.format(value, s)
    return "{0}B".format(n)


def get_cpu_info():
    cpu_count = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent(interval=1)
    return dict(cpu_count=cpu_count, cpu_percent=cpu_percent)

def get_memory_info():
    virtual_mem = psutil.virtual_memory()
    mem_total = bytes2num(virtual_mem.total)
    mem_percent = virtual_mem.percent
    mem_free = bytes2num(virtual_mem.free + virtual_mem.buffers + virtual_mem.cached)
    mem_used = bytes2num(float(virtual_mem.total*virtual_mem.percent*0.01))
    
    return dict(mem_total=mem_total,mem_percent=mem_percent,mem_free=mem_free,mem_used=mem_used)

def get_disk_info():
    disk_usage = psutil.disk_usage('/')
    disk_total = bytes2num(disk_usage.total)
    disk_percent = disk_usage.percent
    disk_free = bytes2num(disk_usage.free)
    disk_used = bytes2num(disk_usage.used)
    
    return dict(disk_total=disk_total,disk_percent=disk_percent,disk_free=disk_free,disk_used=disk_used)

def get_boot_info():
    boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')
    return dict(boot_time=boot_time)

def collect_monitor_data():
    data = {}
    data.update(get_boot_info())
    data.update(get_cpu_info())
    data.update(get_memory_info())
    data.update(get_disk_info())
    return data

def render(tpl_path,**kwargs):
    path,filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(**kwargs)

def main():
    hostname = socket.gethostname()
    data = collect_monitor_data()
    data.update(hostname=hostname)
    content = render('./monitor.html',**data)
    # print(content)
    with yagmail.SMTP(user=EMAIL_USER,password=EMAIL_PASSWORD,host='smtp.163.com') as yag:
        for recevier in RECIPIENTS:
            yag.send(recevier, '监控信息', content)
    

if __name__ == "__main__":
    main()
