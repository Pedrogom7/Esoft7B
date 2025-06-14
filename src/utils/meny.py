def selecionar_acao():
    print("\nSelecione uma opção:")
    print("[1] Inserir novo aluno")
    print("[2] Excluir aluno cadastrado")
    print("[3] Modificar dados do aluno")
    print("[4] Inserir valor categórico")
    print("[5] Concluir cadastro")
    escolha = input("Digite o número da opção desejada: ").strip()
    return escolha