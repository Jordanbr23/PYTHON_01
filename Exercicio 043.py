print('Analise de Triangulos')
s1=int(input('Digite um segmento:'))
s2=int(input('Digite outro segmento:'))
s3=int(input('Digite o último segmento:'))
if s1 == s2 or s1 == s3 or s2 == s3:
    print('Esses segmentos formam um triangulo EQUILÁTERO')
elif s1 != s2 and s1 == s3 or s1 == s2 and s1 != s3:
    print('Esses segmentos formam um triangulo ISOCELES')
elif s1 != s2 and s1 != s3 and s2 !=s3:
    print('Esses segmentos formam um triangulo ESCALENO')