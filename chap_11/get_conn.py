#! /usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql
import os
import json
from contextlib import contextmanager


def get_conn(**kwargs):
    return pymysql.connect(host=kwargs.get('host', 'localhost'),
                           user=kwargs.get('user', 'user1'),
                           passwd=kwargs.get('passwd'),
                           port=kwargs.get('port', 3306),
                           db=kwargs.get('db')
                           )


@contextmanager
def get_conn1(**kwargs):
    conn = pymysql.connect(
        host=kwargs.get('host', 'localhost'),
        user=kwargs.get('user', 'user1'),
        passwd=kwargs.get('passwd'),
        port=kwargs.get('port', 3306),
        db=kwargs.get('db')
    )

    try:
        yield conn
    finally:
        if conn:
            conn.close()


def main():
    # conn = get_conn(host='192.168.32.1', user='user1',
    #                 passwd='user1', db='python_manage')
    # cur = conn.cursor()
    # cur.execute('select * from hosts')
    # # print(cur.fetchall())
    # result = json.dumps(cur.fetchall(), indent=2, sort_keys=True)
    # print(result)

    # cur.close()
    # conn.close()

    my_args = dict(host='192.168.32.1', user='user1',
                   passwd='user1', db='python_manage')
    # print(conn_args)
    with get_conn1(host='192.168.32.1', user='user1',
                   passwd='user1', db='python_manage') as conn:
        with conn as cur:
            cur.execute('select * from hosts')
            print(cur.fetchall())


if __name__ == "__main__":
    main()
