print('EXERCITO BRASILEIRO')
a=int(input('Ano de nascimento:'))
c=2022-a
d= 18-c
e= 2022 + d
f= c -18
print('Quem nasceu em {} tem {} anos'.format(a,c))
if c < 18:
    print('Ainda falta {} anos para seu alistamento'.format(d))
    print('Seu alistamento será em {}'.format(e))
elif c == 18:
    print('2022 é o seu ano de alistamento, apresenta-se no quartel militar mais próximo de voce!')
else:
    print('Voce já se alistou a {} anos em {}'.format(f,e))
