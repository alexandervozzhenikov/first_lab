import math
w = float(input("w="))
y = float(input("y="))
g = ((9.33*w**3)+math.sqrt(w)/(math.log(y+3.5,math.e)+math.sqrt(y)))
print(g)