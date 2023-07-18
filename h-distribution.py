name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
cc=dict()
for line in fh:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    words=line.split()
    word=words[5]
    hour=word.split(':')
    h=hour[0]
    cc[h]=cc.get(h,0)+1
cd=sorted(cc.items())
for k,v in cd:
    print(k,v)