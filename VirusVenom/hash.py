import hashlib
print(hashlib.md5(open('/home/ubuntu/project/check.png','rb').read()).hexdigest())