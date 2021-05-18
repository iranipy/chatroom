import redis
import uuid

r = redis.Redis(host='localhost', port=6379, db=0)


def uid_gen():
    return uuid.uuid4()
