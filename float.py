hrs = input("Enter Hours:")

rate = input("Enter Rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric value")
    quit()
if h<=40:
    Pay=h*r
else :
    Pay=h*r+0.5*r*(h-40)
print(Pay)