import os

tarefas ={
    'tarefas':['tirar pó','lavar a louça'],
    'datas': ['30/06','30/06']
}

def mostrar_tarefas():
    print('-'*15)
    print('|Tarefas:')
    print('-'* 15)
    for i in range(len(tarefas['tarefas'])):
        print(f'|{i+1}.{tarefas['tarefas'][i]} - Data: {tarefas['datas'][i]}')
    print('-' *15)

def adicionar_tarefas():
    tarefa = input('| Digite o nome da tarefa:')
    data = input('| Digite a data: ')
    tarefas['tarefas'].append(tarefa)
    tarefas['datas'].append(data)
    print('| Tarefa adicionada com sucesso!')

def remover_tarefas():
    mostrar_tarefas()
    


def menu():
    while True:
        os.system('cls')
        print('-' *15)
        print('Tarefas:')
        print('-' *15)
        print('| (1) Mostrar tarefas')
        print('| (2) Adicionar tarefas')
        print('| (3) Remover tarefas')
        print('| (4) Sair')
        print('-' *15)
        opcao = int(input('| Escolha uma das opções:'))

        if opcao == 1:
            os.system('cls')
            mostrar_tarefas()
            input('| Pressione para continuar...')

        elif opcao == 2:
            adicionar_tarefas()
            input('| Pressione para continuar...')

        elif opcao == 3:
            print()

        elif opcao == 4:
            print('Encerrando o programa..')
            break

        else:
           print('Opção errada. Escolha uma opção correta...')
         
         
         
          







menu()