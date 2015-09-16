from django.test import TestCase

# Create your tests here.

import redis

r = redis.Redis(host='localhost',port=6379,db=0)
print r.dbsize()
