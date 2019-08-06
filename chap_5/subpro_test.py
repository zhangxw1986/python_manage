#! /usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess


def call_test():
    
    ret_code = subprocess.call('ls -al' ,shell=True)
    print(ret_code)

def check_call_test():
    try:
        ret_code = subprocess.check_call('l -al' ,shell=True)
    except subprocess.CalledProcessError as e:
        print(e)
        print(e.output)
        print(e.cmd)
        print(e.returncode)

def check_output():
    output = subprocess.check_output('df -h',shell=True,stderr=subprocess.STDOUT)
    # print(output)
    for line in output.decode('utf-8').split('\n'):
        print(line.strip())
        
def execute_cmd(cmd):
    '''
    python程序中执行shell语句
    '''
    p = subprocess.Popen(
        cmd,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE   
    )
    stdout,stderr = p.communicate()
    if p.returncode !=0:
        return p.returncode,stderr
    return p.returncode,stdout


if __name__ == "__main__":
    # check_call_test()
    # check_output()
    returncode,output = execute_cmd('ps -ef|grep python')
    print("返回码是{0}".format(returncode))
    for line in output.decode('utf-8').split('\n'):
        print(line.strip())
    