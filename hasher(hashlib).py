import hashlib
filename = 'C:\\Users\\ASH\\Documents\\PyPro2\\1.jpg'
hasher = hashlib.md5()
with open(filename, 'rb') as open_file:
    content = open_file.read()
    hasher.update(content)
print(hasher.hexdigest())

##import os
##filename = 'C:\\Users\\ASH\\Documents\\PyPro\\1.jpg'
##cmd = 'md5sum ' + filename
##fp = os.popen(cmd)
##res = fp.read()
##stat = fp.close()
##print(res)
