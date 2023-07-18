import re
fh = open('regex_sum_833669.txt')
numlist=list()
count = 0
for line in fh:
    line=line.rstrip()
    stuff=re.findall('[0-9]+',line)
    for num in stuff:
        number=int(num)
        numlist.append(number)	
sum_of_no=sum(numlist)
print("Average is = ", sum_of_no)
