# # Aluguel de carros:

# # Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado

# # Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado



# 2 - (km) Pedir a quantidade de km percorridos

# 3 - (valor_dias) Calcular o valor total dos dias (dias * 60)
# 4 - (valor_km) Calcular o valor total da quilometragem (km * 0.15)


# 5 - (valor_total) Calcular o valor total somando o valor dos dias + o valor dos km

# 6 - Mostrar na tela a frase formatada
carro =input('Qual foi o modelo do carro alugado:')
dias =int(input('Por quanto dias o carro foi alugado:'))
km =float(input('Quantos km o carro andou:'))
valor_dia=0
if carro =='gol':
    valor_dia :90

elif carro== 'reno':
    valor_dia: 110

if carro=='Bmw':
   valor_dia= 1000
    
else :
    valor_dia =30





valor_dias=(dias * valor_dia)
valor_km=(km * 0.15)
valor_total = (valor_dias + valor_km)
print (f'Voce andou {valor_km} km por {valor_dias} dias, entao o preço a pagar é: R$ {valor_total}')

