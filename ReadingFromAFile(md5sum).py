import os
filename = 'C:\\Users\\ASH\\Documents\\output.txt'
cmd = 'md5sum ' + filename
fp = os.popen(cmd)
res = fp.read()
#stat = fp.close()
print(res)
#print(stat)
