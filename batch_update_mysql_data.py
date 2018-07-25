#!/usr/bin/env python
# encoding: utf-8
'''
@author: root
@contact: root@mylonly.com
@file: batch_update_mysql_data.py
@time: 2018/7/25 10:48 AM
@desc:
'''


import pymysql
from os import path


connect = pymysql.connect('cd-cdb-drfr0zno.sql.tencentcdb.com', 'root', 'WRX703003659txg', 'recommend', port=63835, charset='utf8mb4', use_unicode=True)
cursor = connect.cursor()
connect.autocommit(True)


sql = 'select id, avatar from cast'

cursor.execute(sql)
results = cursor.fetchall()

upload_results = {}

for result in results:
    id = result[0]
    avatar = result[1]
    key = path.basename(avatar)

    new_url = "http://movie.mylonly.com/%s" % key

    sql = "update cast set avatar='%s' where id = '%s'" % (new_url, id)
    cursor.execute(sql)

