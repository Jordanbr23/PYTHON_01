from math import sqrt
Co=float(input('Qual comprimento do cateto oposto?'))
Ca=float(input('Qual comprimento do cateto adjacente?'))
h=(Co**2 + Ca**2)
r=sqrt(h)
print('Com {}cm e {}cm, a hipotenusa do triangulo será:{:.2f}cm'.format(Co,Ca,r))
