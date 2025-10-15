#Багринцев Даниил Михайлович
#2 вариант
import math
x = -4.5
y = 0.75 * math.pow(10,-4);
z = -0.845*math.pow(10, 2)
s = (((9+(x-y)**2) ** (1.0/3.0))/((x**2)+(y**2)+2)) - (math.exp(math.fabs(x - y)))*(math.pow(math.tan(z),3))
print(s)
