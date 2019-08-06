#! /usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import json
from collections import defaultdict
from contextlib import contextmanager
import pymysql


def to_json(in_dict):
    # return json.dumps(in_dict, sort_keys=True, indent=2)
    return json.dumps(in_dict,indent=2,sort_keys=True)

@contextmanager
def get_conn(**kwargs):
    conn = pymysql.connect(**kwargs)
    try:
        yield conn
    finally:
        conn.close()

def parse_args():
    parser = argparse.ArgumentParser(description='CMDB inventory module')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--list', action='store_true',
                       help='List active servers')
    group.add_argument('--host', help='List details about the specific host')
    return parser.parse_args()

def list_all_hosts(conn):
    hosts = defaultdict(list)

    with conn as cur:
        cur.execute('select * from hosts')
        rows = cur.fetchall()
        for row in rows:
            no, host, group, user, port = row
            hosts[group].append(host)
    return hosts

def get_host_detail(conn, host):
    details = {}
    with conn as cur:
        cur.execute("select * from hosts where host = '{0}'".format(host))
        rows = cur.fetchall()
        if rows:
            no, host, group, user, port = rows[0]
            details.update(ansible_user=user, ansible_port=port)
    return details


def main():
    parser = parse_args()
    with get_conn(host='192.168.32.1', user='user1', passwd='user1', db='python_manage') as conn:
        if parser.list:
            hosts = list_all_hosts(conn)
            # print(to_json(hosts))
            print(to_json(hosts))
        else:
            details = get_host_detail(conn, parser.host)
            print(to_json(details))


if __name__ == '__main__':
    main()
