name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
counts=dict()
for line in fh:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    words=line.split()
    word=words[1]
    counts[word]=counts.get(word,0)+1
bigcount=None
bigword=None
for k,v in counts.items():
    if bigcount is None or v>bigcount:
        bigword=k
        bigcount=v
print(bigword,bigcount)