#!/usr/bin/env python
# encoding: utf-8

'''
@author: root
@contact: root@mylonly.com
@file: qiniu_upload_online_image.py
@time: 2018/7/25 9:58 AM
@desc: 利用七牛SDK上传网络图片至七牛存储空间
'''


from qiniu import Auth
from qiniu import BucketManager
import pymysql
from os import path


connect = pymysql.connect('cd-cdb-drfr0zno.sql.tencentcdb.com', 'root', 'WRX703003659txg', 'recommend', port=63835, charset='utf8mb4', use_unicode=True)
cursor = connect.cursor()
connect.autocommit(True)

access_key = 'DbWGs0o6YeNfI37DU1TukHaDfAXtSU0oKKBxTO4T'
secret_key = 'sTt5UNv956CwSS6itU0D2nJ3J01bscUKxPMP4cE7'

bucket_name = 'movierec'

q = Auth(access_key, secret_key)
bucket = BucketManager(q)

sql = 'select id, avatar from cast'

cursor.execute(sql)
results = cursor.fetchall()

upload_results = {}

for result in results:
    id = result[0]
    avatar = result[1]
    key = path.basename(avatar)
    ret, info = bucket.fetch(avatar, bucket_name, key)
    assert ret['key'] == key
    upload_results[id] = "http://movie.mylonly.com/%s" % key

print(upload_results)

