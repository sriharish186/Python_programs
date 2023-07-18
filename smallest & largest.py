largest = None
smallest = None
while True:
    
    num = input('Enter a number: ')
    if num == 'done' : 
        break

    try :
	    fval=int(num)
    
    except :
	    print('Invalid input')
	    continue
    if largest=='None':
        largest=fval
    elif fval>largest:
        largest=fval
    if (smallest is not 'None')&(fval<smallest):
        smallest=fval
    elif (fval>smallest)&(type(smallest)!=int):
        smallest=fval

print("Maximum is", largest)
print("Minimum is", smallest)
