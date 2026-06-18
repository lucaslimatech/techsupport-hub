from gerenciador import GerenciadorChamados


def exibir_menu():
    print("\n========== TECHSUPPORT HUB ==========")
    print("1. Abrir chamado")
    print("2. Listar chamados")
    print("3. Buscar chamado por ID")
    print("4. Atualizar status")
    print("5. Alterar prioridade")
    print("6. Excluir chamado")
    print("0. Sair")
    print("=====================================")


def exibir_chamado(chamado):
    print("\n-------------------------------------")
    print(f"ID: {chamado.id}")
    print(f"Cliente: {chamado.cliente}")
    print(f"Título: {chamado.titulo}")
    print(f"Descrição: {chamado.descricao}")
    print(f"Prioridade: {chamado.prioridade}")
    print(f"Status: {chamado.status}")
    print(f"Data de criação: {chamado.data_criacao}")
    print("-------------------------------------")


def abrir_chamado(gerenciador):
    print("\n--- Abrir novo chamado ---")

    cliente = input("Nome do cliente: ")
    titulo = input("Título do chamado: ")
    descricao = input("Descrição do problema: ")

    print("\nPrioridade:")
    print("1. Baixa")
    print("2. Média")
    print("3. Alta")
    print("4. Crítica")

    opcao_prioridade = input("Escolha a prioridade: ")

    prioridades = {
        "1": "Baixa",
        "2": "Média",
        "3": "Alta",
        "4": "Crítica"
    }

    prioridade = prioridades.get(opcao_prioridade, "Média")

    chamado = gerenciador.abrir_chamado(cliente, titulo, descricao, prioridade)

    print("\nChamado aberto com sucesso!")
    exibir_chamado(chamado)


def listar_chamados(gerenciador):
    print("\n--- Lista de chamados ---")

    chamados = gerenciador.listar_chamados()

    if not chamados:
        print("Nenhum chamado cadastrado.")
        return

    for chamado in chamados:
        exibir_chamado(chamado)


def buscar_chamado(gerenciador):
    print("\n--- Buscar chamado ---")

    try:
        id_chamado = int(input("Digite o ID do chamado: "))
    except ValueError:
        print("ID inválido. Digite apenas números.")
        return

    chamado = gerenciador.buscar_chamado_por_id(id_chamado)

    if chamado:
        exibir_chamado(chamado)
    else:
        print("Chamado não encontrado.")


def atualizar_status(gerenciador):
    print("\n--- Atualizar status ---")

    try:
        id_chamado = int(input("Digite o ID do chamado: "))
    except ValueError:
        print("ID inválido. Digite apenas números.")
        return

    print("\nStatus disponíveis:")
    print("1. Aberto")
    print("2. Em andamento")
    print("3. Resolvido")
    print("4. Fechado")

    opcao_status = input("Escolha o novo status: ")

    status_opcoes = {
        "1": "Aberto",
        "2": "Em andamento",
        "3": "Resolvido",
        "4": "Fechado"
    }

    novo_status = status_opcoes.get(opcao_status)

    if not novo_status:
        print("Opção inválida.")
        return

    sucesso = gerenciador.atualizar_status(id_chamado, novo_status)

    if sucesso:
        print("Status atualizado com sucesso!")
    else:
        print("Chamado não encontrado.")


def alterar_prioridade(gerenciador):
    print("\n--- Alterar prioridade ---")

    try:
        id_chamado = int(input("Digite o ID do chamado: "))
    except ValueError:
        print("ID inválido. Digite apenas números.")
        return

    print("\nPrioridades disponíveis:")
    print("1. Baixa")
    print("2. Média")
    print("3. Alta")
    print("4. Crítica")

    opcao_prioridade = input("Escolha a nova prioridade: ")

    prioridade_opcoes = {
        "1": "Baixa",
        "2": "Média",
        "3": "Alta",
        "4": "Crítica"
    }

    nova_prioridade = prioridade_opcoes.get(opcao_prioridade)

    if not nova_prioridade:
        print("Opção inválida.")
        return

    sucesso = gerenciador.alterar_prioridade(id_chamado, nova_prioridade)

    if sucesso:
        print("Prioridade alterada com sucesso!")
    else:
        print("Chamado não encontrado.")


def excluir_chamado(gerenciador):
    print("\n--- Excluir chamado ---")

    try:
        id_chamado = int(input("Digite o ID do chamado: "))
    except ValueError:
        print("ID inválido. Digite apenas números.")
        return

    confirmar = input("Tem certeza que deseja excluir este chamado? (s/n): ")

    if confirmar.lower() != "s":
        print("Exclusão cancelada.")
        return

    sucesso = gerenciador.excluir_chamado(id_chamado)

    if sucesso:
        print("Chamado excluído com sucesso!")
    else:
        print("Chamado não encontrado.")


def main():
    gerenciador = GerenciadorChamados()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            abrir_chamado(gerenciador)
        elif opcao == "2":
            listar_chamados(gerenciador)
        elif opcao == "3":
            buscar_chamado(gerenciador)
        elif opcao == "4":
            atualizar_status(gerenciador)
        elif opcao == "5":
            alterar_prioridade(gerenciador)
        elif opcao == "6":
            excluir_chamado(gerenciador)
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
