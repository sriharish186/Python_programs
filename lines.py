fh=open('script.txt')
fa=open('op.txt','w')
for line in fh:
    if line.rstrip():
        fa.write(line)
