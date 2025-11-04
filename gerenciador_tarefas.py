# Lista que armazenará todas as tarefas cadastradas pelo usuário,Cada tarefa será um dicionário com 'tarefa' e 'concluida'.
tarefas = []

# Função para adicionar uma nova tarefa
def adicionar_tarefa():
    # Solicita ao usuário que digite a tarefa
    tarefa = input("Digite a nova tarefa: ")
    
    # Adiciona a tarefa na lista como um dicionário, inicializando 'concluida' como False
    tarefas.append({"tarefa": tarefa, "concluida": False})
    
    # Mensagem de confirmação de sucesso
    print("✅ Tarefa adicionada com sucesso!\n")

# Função para mostrar todas as tarefas cadastradas
def mostrar_tarefas():
    # Verifica se a lista de tarefas está vazia
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
        return  # Sai da função se não houver tarefas
    
    # Cabeçalho da lista de tarefas
    print("📋 Lista de Tarefas:")
    
    # Percorre a lista de tarefas, retornando índice (i) e a tarefa (t)
    for i, t in enumerate(tarefas, 1):  # Começa a contagem do índice em 1
        # Define o status da tarefa: ✔️ se concluída, ❌ se não concluída
        status = "✔️" if t["concluida"] else "❌"
        # Exibe o número, a descrição da tarefa e o status
        print(f"{i}. {t['tarefa']} - {status}")
    
    # Linha em branco para separar a saída
    print()

# Função para marcar uma tarefa como concluída
def concluir_tarefa():
    # Mostra todas as tarefas antes de pedir a seleção
    mostrar_tarefas()
    
    try:
        # Solicita ao usuário o número da tarefa a ser concluída
        num = int(input("Digite o número da tarefa concluída: "))
        
        # Marca a tarefa selecionada como concluída
        tarefas[num-1]["concluida"] = True
        
        # Mensagem de confirmação
        print("🎯 Tarefa marcada como concluída!\n")
    
    # Trata casos de entrada inválida (não número ou índice fora da lista)
    except (ValueError, IndexError):
        print("Número inválido.\n")

# Função para excluir uma tarefa
def excluir_tarefa():
    # Mostra todas as tarefas antes de pedir a seleção
    mostrar_tarefas()
    
    try:
        # Solicita ao usuário o número da tarefa a ser removida
        num = int(input("Digite o número da tarefa a excluir: "))
        
        # Remove a tarefa selecionada da lista
        tarefas.pop(num-1)
        
        # Mensagem de confirmação
        print("🗑️ Tarefa removida!\n")
    
    # Trata casos de entrada inválida (não número ou índice fora da lista)
    except (ValueError, IndexError):
        print("Número inválido.\n")

# Função que exibe o menu principal do gerenciador
def menu():
    while True:  # Loop infinito até o usuário decidir sair
        # Cabeçalho do menu
        print("==== GERENCIADOR DE TAREFAS ====")
        print("1. Adicionar tarefa")
        print("2. Mostrar tarefas")
        print("3. Concluir tarefa")
        print("4. Excluir tarefa")
        print("5. Sair")
        
        # Solicita a escolha do usuário
        opcao = input("Escolha uma opção: ")

        # Avalia a opção e chama a função correspondente
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            mostrar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            excluir_tarefa()
        elif opcao == "5":
            # Sai do loop e encerra o programa
            print("Saindo... 👋")
            break
        else:
            # Mensagem de erro caso a opção seja inválida
            print("Opção inválida.\n")

# Ponto de entrada do programa
# Garante que o menu só será executado se o arquivo for rodado diretamente
if __name__ == "__main__":
    menu()



