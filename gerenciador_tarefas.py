tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append({"tarefa": tarefa, "concluida": False})
    print("✅ Tarefa adicionada com sucesso!\n")

def mostrar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
        return
    print("📋 Lista de Tarefas:")
    for i, t in enumerate(tarefas, 1):
        status = "✔️" if t["concluida"] else "❌"
        print(f"{i}. {t['tarefa']} - {status}")
    print()

def concluir_tarefa():
    listar_tarefas()
    try:
        num = int(input("Digite o número da tarefa concluída: "))
        tarefas[num-1]["concluida"] = True
        print("🎯 Tarefa marcada como concluída!\n")
    except (ValueError, IndexError):
        print("Número inválido.\n")

def excluir_tarefa():
    mostrar_tarefas()
    try:
        num = int(input("Digite o número da tarefa a excluir: "))
        tarefas.pop(num-1)
        print("🗑️ Tarefa removida!\n")
    except (ValueError, IndexError):
        print("Número inválido.\n")

def menu():
    while True:
        print("==== GERENCIADOR DE TAREFAS ====")
        print("1. Adicionar tarefa")
        print("2. Mostrar tarefas")
        print("3. Concluir tarefa")
        print("4. Excluir tarefa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            mostrar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            excluir_tarefa()
        elif opcao == "5":
            print("Saindo... 👋")
            break
        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    menu()
