#! /usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql
import argparse
import string
import threading
import random
import time
from contextlib import contextmanager

DB_NAME = 'python_manage'
DB_TABLE = 'test_insert_data_table'
CREATE_TABLE_SQL = '''create table test_insert_data_table(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(23) NOT NULL,
    time double NOT NULL);
'''


def _argparse():
    parser = argparse.ArgumentParser(
        description='benchmark tool for mysql database. ')
    parser.add_argument('--host', action='store', dest='host',
                        required=True, help='connect to the host.')
    parser.add_argument('--user', action='store', dest='user',
                        required=True, help='user for login.')
    parser.add_argument('--port', action='store', dest='port', default=3306,
                        type=int, help='port number to use for connection or 3306 default.')
    parser.add_argument('--passwd', action='store', dest='password',
                        required=True, help='password  for user login.')
    parser.add_argument('--thread_size', action='store', dest='thread_size',
                        default=5, type=int, help='how much connection for database usage.')
    parser.add_argument('--row_size', action='store', dest='row_size',
                        default=5000, type=int, help='how much rows.')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 0.1')
    return parser.parse_args()


@contextmanager
def get_conn(**kwargs):
    conn = pymysql.connect(**kwargs)
    try:
        yield conn
    finally:
        conn.close()



def create_table(conn):
    
    use_db = 'use python_manage'
    del_table_sql = 'drop table if exists {0}'.format(DB_TABLE)

    with conn as cur:
        for sql in [use_db,del_table_sql, CREATE_TABLE_SQL]:
            print(sql)
            cur.execute(sql)


def random_string(length=10):
    s = string.ascii_letters + string.digits
    return "".join(random.sample(s, length))


def add_row(cursor):
    SQL_FORMAT = "INSERT INTO {0}(name,time) values('{1}',{2})"
    sql = SQL_FORMAT.format(DB_TABLE, random_string(), time.time())
    cursor.execute(sql)


def insert_data(conn_args, row_size):
    with get_conn(**conn_args) as conn:
        with conn as cur:
            cur.execute('use {0}'.format(DB_NAME))
        with  conn as cur:
            for t in range(row_size):
                add_row(cur)
                conn.commit()


def main():
    parser = _argparse()
    conn_args = dict(host=parser.host, user=parser.user,
                     password=parser.password, port=parser.port)
    with get_conn(**conn_args) as conn:
        create_table(conn)

    threads = []
    for t in range(parser.thread_size):
        t = threading.Thread(target=insert_data,
                             args=(conn_args, parser.row_size))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()

    # python insert_data.py --host=192.168.32.1 --port=3306 --user=root --passwd=root
