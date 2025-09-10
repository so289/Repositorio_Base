quantidade_filmes =int(input('Digite a quantidade de filmes:'))
contador= 1
filmes = []
while contador<= quantidade_filmes:
    nome_filme= input('Digite o nome do filme:')
    contador= contador+1
    filmes.append(nome_filme)

print (filmes)