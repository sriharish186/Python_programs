num=0
tot=0
l1=[]
while True:
    
    sval=input('Enter a number for the list; If you are done enter done ')
    if sval=='done' :
        break
	try:
	     fval=int(sval)
	 except:
	     print('Invalid input')
		 continue
	 l1=list.append(fval)

if num==0:
    num=1	 
print(l1)
