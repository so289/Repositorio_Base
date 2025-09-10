# Calcule a média das notas utilizando um loop while e também um loop for


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

notas = ['9.5', '10', '6.75', '5.5']

# LOOP WHILE
cont =0
soma =0
while cont<len(notas):
    soma = soma + float(notas[cont])
    cont = cont + 1
    


media = soma / cont
print (media)


print()



# LOOP FOR
soma =0
for nota in  notas:
    soma = soma + float(nota)

media = soma /len(notas) 

print(media)

