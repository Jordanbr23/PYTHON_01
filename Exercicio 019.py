import math
x=float(input('Digite um angulo:'))
s=math.asin(math.radians(x))
c=math.acos(math.radians(x))
t=math.atan(math.radians(x))
print('O seno de {} é:{:.2f}\n O cosseno de {} é:{:.2f}\n A tangente de {} é:{:.2f}'.format(x,s,x,c,x,t))