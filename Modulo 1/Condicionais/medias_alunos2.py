print('SISTEMA DE PROVAS ')
print('')
contador=1
prova =int(input('Quantas provas o aluno realizou: '))
soma=0
while contador <= prova:
    nota= float(input(f'Qual é a nota da prova {contador}: '))
    soma= soma+ nota
    contador= contador+1

media= soma/prova
print(f'Média: {media:.2f}')
