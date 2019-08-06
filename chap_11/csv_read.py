#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
读取csv文件
'''

import csv
from collections import namedtuple
from contextlib import contextmanager
import pymysql


def read_csv():
    '''读取CSV数据'''
    with open('1.csv', 'r') as f:
        f_csv = csv.reader(f)
        heads = next(f_csv)
        Row = namedtuple('Row', heads)
        for row in f_csv:
            yield Row(*row)


@contextmanager
def get_conn1(**kwargs):
    '''获取数据库连接 '''
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


def exec_sql(conn, sql):
    with conn as cur:
        cur.execute(sql)


def main():
    SQL_FORMAT = '''insert into hosts values({0},'{1}','{2}','{3}',{4})'''
    with get_conn1(host='192.168.32.1', user='user1', passwd='user1', db='python_manage') as conn:
        for row in read_csv():
            sql = SQL_FORMAT.format(
                row.id, row.host, row.groupname, row.username, row.port)
            exec_sql(conn, sql)


if __name__ == "__main__":
    main()
