import hashlib


def hash_str(str):
    m = hashlib.sha256()
    m.update(str.encode('utf-8'))
    return m.hexdigest()
