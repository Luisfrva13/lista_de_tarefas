# CRIAR UM PROGRAMA QUE FAÇA UMA LISTA DE TAREFAS PARA O USUÁRIO
import os
# lista vazia

tarefas = []

# laço de repetição

while True:
    # usuário vai informar a tarefa
    
    nova_tarefa = input('Informe a nova tarefa ou deixe vazio para encerrar e exibir a lista:')

    # verificar se eo usuário inseriu a nova tarefa
    
    if nova_tarefa != '':
        tarefas.append(nova_tarefa)
        continue
    else:
        break
# Limpar console

os.system('cls')

# imrpimir a lista

for tarefa in tarefas:
    print(tarefa)