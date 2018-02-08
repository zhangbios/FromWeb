import hashlib


test_md5 = hashlib.md5()
test_md5.update(b"Nobody inspects the spammish repetition")
test_md5_digest = test_md5.hexdigest()
print(test_md5_digest)