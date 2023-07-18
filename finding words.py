fname = input("Enter file name: ")
fh = open(fname)
lst = list()
a=len(lst)
#print(a)
#print(lst[0])
for line in fh:
    line=line.rstrip()
    line=line.split()
    #if len(lst)==0:
    #index=0    
    for wor in line:
        index2=0
        #print(line[index])
        if a==0:
            lst.append(wor)
            a=a+1
            #print(lst)
        else:
            b=0
            for word in lst:
                if (word == wor):
                    b=1
                    continue
                    #b=1
                #else:
                    #word2=line[index]
                    #lst.append(word2)
                    #print(lst)
                #index2=index2+1
            if b==0:
                lst.append(wor)
        #index=index+1
lst.sort()
print(lst)
