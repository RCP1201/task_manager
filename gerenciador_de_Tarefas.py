#Projeto: Gerenciador de Tarefas
#Descrição:
#Vamos criar um gerenciador de tarefas simples que permitirá ao usuário adicionar, visualizar e marcar tarefas como concluídas.

#Funcionalidades:
#Adicionar uma nova tarefa.
#Visualizar todas as tarefas.
#Marcar uma tarefa como concluída.

#Requisitos:
#O programa deve solicitar ao usuário que escolha uma opção do menu principal.
#O programa deve armazenar as tarefas em uma lista.
#Para marcar uma tarefa como concluída, o usuário deve inserir o número da tarefa na lista.
#Após realizar uma operação, o programa deve exibir novamente o menu principal.
#Sugestões para a implementação:
#Use loops para exibir o menu principal e solicitar a entrada do usuário.
#Use listas para armazenar as tarefas.
#Utilize funções para organizar o código e realizar operações específicas (adicionar tarefa, exibir tarefas, marcar tarefa como concluída).
#Considere usar um loop infinito para manter o programa em execução até que o usuário opte por sair.
#Adicional: lista tarefas concluídas


class tarefas:
    def __init__(self, task, vertarefa, concluida):
        self.task = task
        self.vertarefa = vertarefa
        self.concluida = concluida
    def incluir(self):
        print("Tarefa, ", self.task, " inclusa com sucesso")
    def mostra(self):
        print("Essa são suas tarefas cadastradas: ", self.vertarefa)
    def conclui(self):
        print("Tarefa, ", self.concluida, "concluída com sucesso")

task =""
vertarefa = ""
concluida = ""


print("Bem vindo ao seu gerenciador de tarefas\n")
lista_tarefas = []
fechaapp = "Não"

while fechaapp.lower() == "não":
    print(
          "Escolha uma das opções:\n\n",
          "1 - Adicionar uma tarefa\n",
          "2 - Mostrar todas as tarefas\n",
          "3 - Concluir uma tarefa\n"
          )
    escolha = input("Digite o número do serviço: ")
    if escolha == "1":
        task = input("Digite a tarefa que deseja adicionar: ").lower()
        lista_tarefas.append(task)
        tarefa = tarefas(task, vertarefa, concluida)
        tarefa.incluir()
        
    elif escolha == "2":
        if not lista_tarefas:
            print("Você não tem tarefas cadastradas!")
            
        else:
            print("Essas são suas tarefas: ", lista_tarefas)
            

    elif escolha == "3":
        concluida = input("Digite a tarefa a ser concluida: ").lower()
        #concluida = concluida.lower()
        if concluida in lista_tarefas:
           lista_tarefas.remove(concluida)
           removida = tarefas(concluida, vertarefa, concluida)
           removida.conclui()
        else:
           print("Tarefa não encontrada!")
    else:
        print("Escolha uma opção válida")
    fechaapp = input("Fechar aplicativo? ")
























    