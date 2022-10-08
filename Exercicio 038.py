n=int(input('Digite um Número inteiro:'))
print('''Escolha uma das bases para conversão:
[1] convertar para binário
[2] converter para octal
[3] converter para hexadecimal''')
opção=int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para Binário é igual a {}'.format(n,bin(n)))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format(n,oct(n)))
else:
    print('{} convertido para hexadecimal é igual a {}'.format(n,hex(n)))

