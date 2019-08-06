#!/user/bin/env python
# coding=utf-8

import pymysql

    db = pymysql.connect("localhost","root","root","test")
    cur = db.cursor()
    sql = "select 1"
    cur.execute(sql)
    rows = cur.fetchall()
    print(rows)

