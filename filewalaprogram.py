import os

def makeTempFiles(fin):
    tnames = []
    done = False
    while not done:
        tn = makeTempFiles()
        tnames.append(tn)
        fn = open(tn, 'w')
        lines = []
        I = 0
        while not done and I < 100:
            I = I + 1
            line = fin.readline()
            if line:
                lines.append(line)
            else:
                done = True

        lines.sort()
        fn.writelines(lines)
        fn.close()
    return tnames

try:
    fin = open("input.txt")
except IOERROR:
    print('Unable to open the file...')
else:
    tlist = makeTempFiles(fin)
while len(tlist):
    mergetTwoIntoOne(tlist)
tname = tlist.pop()
os.rename(tname, 'output.txt')
