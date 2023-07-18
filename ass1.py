
from os import lstat


def q4():
	def help(x):
		return x % 2 == 0

	lst = [i**2 for i in range(10)] 
    #a=10
lst = filter(help, lst)
print(list(lst))
    #print(lst)

q4()