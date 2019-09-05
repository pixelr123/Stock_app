import redis
import os

REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
BHAV_COPY_URL = "https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx"

def get_redis_connection():
    res = {"status": 0, "data": ""}
    try:
        #r = redis.StrictRedis(host='REDISTOGO_URL',charset="utf-8",decode_responses=True, port=6379, db=0)
        r = redis.from_url(os.environ.get("REDISTOGO_URL"), charset="utf-8", decode_responses=True, db=0)
        res["status"] = 1
        res["data"] = r
    except Exception as e:
        res["data"] = "Redis connection error"
    return res

