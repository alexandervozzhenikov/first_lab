import math
t = -6
x = float(input("x="))
a = math.log(x)
b = math.sqrt(x**2+t**2)
y = math.sqrt(abs(a-b*x))**(1/5)
print("a=",a," b=",b," y=",y)