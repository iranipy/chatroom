import os
import redis
import uuid

from cryptography.fernet import Fernet

r = redis.Redis(host='localhost', port=6379, db=0)


def uid_gen():
    return uuid.uuid4()


def load_key():
    return open("secret.key", "rb").read()


def str_encryption(text: str, enc: bool = None, dec: bool = None):
    key = load_key()
    f = Fernet(key)
    if enc:
        return f.encrypt(text.encode())

    return f.decrypt(text).decode()
