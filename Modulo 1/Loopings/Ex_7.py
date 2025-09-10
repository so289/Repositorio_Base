# Crie uma lista com 3 dicionários, cada um representando uma pessoa (contendo nome, idade, cidade). Use um laço para imprimir o nome de cada pessoa.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
nomes = [ {'Nome' : 'Mariana', 'Idade' : '23','Cidade' :'Cajamar' },
          {'Nome' : 'Joaquim', 'Idade' : '33','Cidade' :'Campinas' },
          {'Nome' : 'Matheus ','Idade' : '40','Cidade' :'Minas Gerais' } 
]

for dados in nomes:
    print(f'Nome: {dados['Nome']}')