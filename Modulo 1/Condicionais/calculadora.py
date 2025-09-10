print ('Calculadora')

print('1-soma')
print('2-subtracao')
print('3-multiplicacao')
print('4- divicao')
opcoes=int(input('digite uma das opcoes:'))
n1=int(input('digite o primeiro numero:'))
n2=int(input('digite o segundo numero:'))

if opcoes == 1:
    print('resultado:',n1+n2)
if opcoes== 2:
    print('resultado;',n1-n2)
if opcoes == 3:
    print('resultado:' ,n1*n2)
if opcoes == 4 :
    print('resultado:' ,n1/n2)
