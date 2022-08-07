import redis
import os

r = redis.Redis(host=os.environ["REDIS_HOST"], port=os.environ["REDIS_PORT"], db=0)