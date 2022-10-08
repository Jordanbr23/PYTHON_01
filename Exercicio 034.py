s=float(input('Qual o salário do funcionário?R$'))
if s>1.250:
    a= (s*10/100)+s
    print('O salário com o aumento de 10% será de {:.3f}R$'.format(a))
else:
    d= (s*15/100)+s
    print('O salário com aumento de 15% será de {:.3f}R$'.format(d))
print('---'*80)
print('CHRONOS INFORMÁTICA')