# Utilize um loop while e um loop for para adicionar itens na lista.
# Peça para que o usuário digite quantos filmes deseja adicionar, e também os nomes dos filmes



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

filmes = [] # Não apague esta lista

# LOOP WHILE

filme_adc= int (input('Quantos filmes você quer adicionar:'))
cont = 1 
filmes= []
while cont <= filme_adc:
    nome_filme =input('Digite o nome do filme:')
    cont = cont +1 
    filmes.append(nome_filme)

    print(filmes)


print()
# LOOP FOR

filme_adc= int (input('Quantos filmes você quer adicionar:'))
cont = 0
filme=[] 

for filmes in  range(filme_adc):
    nome_filme = input(' Digite o nome do filme: ')
    cont = cont +1
    filme.append(nome_filme)

print(filme)



