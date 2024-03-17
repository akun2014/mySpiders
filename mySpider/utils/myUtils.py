import hashlib


def hash_str(h_str):
    if not h_str:
        return None
    m = hashlib.sha256()
    m.update(h_str.encode('utf-8'))
    return m.hexdigest()
