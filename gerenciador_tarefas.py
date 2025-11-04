# Lista que armazenará todas as tarefas cadastradas pelo usuário.
tarefas = [] # Lista que armazenará todas as tarefas cadastradas pelo usuário.

def adicionar_tarefa():# Função para adicionar uma nova tarefa
    tarefa = input("Digite a nova tarefa: ")  # Solicitar ao usuário que digite uma tarefa
    tarefas.append({"tarefa": tarefa, "concluida": False})  # Adiciona a tarefa na lista como um dicionário, inicializando 'concluida' como False
    print("✅ Tarefa adicionada com sucesso!\n")

def mostrar_tarefas():# Função para mostrar todas as tarefas cadastradas
    if not tarefas: # Verifica se a lista de tarefas está vazia
        print("Nenhuma tarefa cadastrada.\n")
        return  # Sai da função se não houver tarefas
    print("📋 Lista de Tarefas:")
    # Percorre a lista de tarefas, retornando índice (i) e a tarefa (t)
    for i, t in enumerate(tarefas, 1): # Começa a contagem do índice em 1
        # Define o status da tarefa: ✔️ se concluída, ❌ se não concluída
        status = "✔️" if t["concluida"] else "❌"
        # Exibe o número, a descrição da tarefa e o status
        print(f"{i}. {t['tarefa']} - {status}")
    print()

def concluir_tarefa(): # Função para marcar uma tarefa como concluída
     mostrar_tarefas()  # Mostra todas as tarefas antes de pedir a seleção
    try:
        num = int(input("Digite o número da tarefa concluída: ")) # Solicita ao usuário o número da tarefa a ser concluída
        tarefas[num-1]["concluida"] = True    # Marca a tarefa selecionada como concluída
        print("🎯 Tarefa marcada como concluída!\n") # Mensagem de confirmação
    except (ValueError, IndexError):
        print("Número inválido.\n")   # Trata casos de entrada inválida
        
def excluir_tarefa(): # Função para excluir uma tarefa 

    mostrar_tarefas()  # Mostra todas as tarefas antes de pedir a seleção
    try:
        num = int(input("Digite o número da tarefa a excluir: "))   # Solicita ao usuário o número da tarefa a ser removida
        tarefas.pop(num-1)  # Remove a tarefa selecionada da lista
        print("🗑️ Tarefa removida!\n")
    except (ValueError, IndexError):
        print("Número inválido.\n")

def menu():# Função que exibe o menu principal do gerenciador
    while True: # Loop infinito até o usuário decidir sair
        print("==== GERENCIADOR DE TAREFAS ====")
        print("1. Adicionar tarefa")
        print("2. Mostrar tarefas")
        print("3. Concluir tarefa")
        print("4. Excluir tarefa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ") # Solicita a escolha do usuário

        if opcao == "1":  # Avalia a opção e chama a função correspondente
            adicionar_tarefa()
        elif opcao == "2":
            mostrar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            excluir_tarefa()
        elif opcao == "5":
            print("Saindo... 👋")   # Sai do loop e encerra o programa
            break
        else:
            print("Opção inválida.\n")    # Mensagem de erro caso a opção seja inválida

# Ponto de entrada do programa
# Garante que o menu só será executado se o arquivo for rodado diretamente
if __name__ == "__main__":
    menu()
