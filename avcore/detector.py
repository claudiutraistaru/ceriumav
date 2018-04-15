import hashlib
def detect(filename):
    hash_data=hashlib.md5()
    with open(filename,'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_data.update(chunk)
    return hash_data.hexdigest()