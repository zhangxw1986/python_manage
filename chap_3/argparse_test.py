# -*- coding:utf-8 -*-

import argparse

def _argsparse():
    parser = argparse.ArgumentParser(description='a Python-MySQL client')
    parser.add_argument('--host',action='store',dest="host",required=True,help='required,connect to host')
    parser.add_argument('-u','--user',action='store',dest='user',required=True,help='required,user for login')
    parser.add_argument('-P','--password',action='store',dest='password',required=True,help='required,password for user')
    parser.add_argument('-p','--port',action='store',dest='port',default=3306,type=int,help='port for connect mysql')
    parser.add_argument('-v','--version',action='version',version='%(prog)s 0.1')
    return parser.parse_args()

def main():
    parser = _argsparse()
    conn_args=dict(host=parser.host,user=parser.user,password=parser.password,port=parser.port)
    print(conn_args)

if __name__ == "__main__":
    main()

