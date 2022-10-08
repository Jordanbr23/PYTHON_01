v=float(input('Qual sua velocidade atual?'))
if v>80:
    print('MULTADO, VOCE ULTRAPASSOU O LIMITE DE VELOCIDADE PERMITIDO QUE É DE 80 KM/H')
    multa=(v-80)*7
    print('SUA MULTA SERÁ DE {}'.format(multa))
else:
    print('O senhor está dentro do limite permitido!')
print('Tenha um bom dia,dirija com segurança')
print('---'*20)
print('DETRAN RN')


