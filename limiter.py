
import redis
import time
import os

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
r = redis.Redis.from_url(redis_url)

MAX_REQUESTS = 5
WINDOW_SECONDS = 60

def is_rate_limited(ip):
    key = f"rate_limit:{ip}"
    now = int(time.time())

    r.zremrangebyscore(key, 0, now - WINDOW_SECONDS)
    current_count = r.zcard(key)

    if current_count >= MAX_REQUESTS:
        return True

    r.zadd(key, {str(now): now})
    r.expire(key, WINDOW_SECONDS)
    return False
