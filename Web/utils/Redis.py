# -*- coding:utf-8 -*-
'''
通过python操作redis
'''

import redis
from django.conf import settings

# 创建redis连接池(默认连接池最大连接数 2**31=2147483648)
pool = redis.ConnectionPool(host='169.254.73.165', port=6379, password=settings.REDIS_PASSWORD, encoding='utf-8',
                            max_connections=1000)
# 从连接池中获取一个链接
conn = redis.Redis(connection_pool=pool)
# 设置键值:18225078646='9999' 且超时时间为60秒(值写入到redis会自动转换成字符串)
conn.set('18225078646', 9999, ex=60)

# 根据键获取值:如果存在获取值(获取到的是字节类型);不存在则返回None
value = conn.get('18225078646')
print(value)
