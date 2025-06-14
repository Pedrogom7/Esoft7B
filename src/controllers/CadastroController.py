from src.models.elemento import Elemento as Pessoa
from src.models.elementoCateg import ElementoCateg as Categoria
from src.models.cluster import Cluster as Agrupamento, distancia_euclidiana as calcular_distancia
from src.utils.menu import menu_acao as menu_opcao
from src.utils.limpar_tela import limpar_tela as limpar_tela_terminal

mapeamento_strings = {}

def ler_float(mensagem):
    entrada = input(mensagem).strip()
    if not entrada:
        return None
    try:
        return float(entrada)
    except ValueError:
        print("Valor inválido. O valor anterior será mantido.")
        return None

def mostrar_clusters(lista_clusters):
    print("\n--- Clusters Gerados ---")
    for grupo in lista_clusters:
        centroide = [round(coord, 2) for coord in grupo.centroide] if grupo.centroide else None
        print(f"Agrupamento {grupo.id} - Centro: {centroide}")
        for item in grupo.elementos:
            marcador = " (Centro)" if item.is_centroide else ""
            if hasattr(item, 'nome'):
                print(f"  {item.nome}: [{item.idade}, {item.falta}, {item.nota}]{marcador}")
            elif hasattr(item, 'valor_str'):
                print(f"  {item.valor_str}: [{item.valor_num}]{marcador}")
        print()

def alocar_em_cluster(entidade, grupos, max_dist):
    qtd_total = sum(len(g.elementos) for g in grupos) + 1

    if qtd_total == 1:
        novo = Agrupamento(1)
        novo.adicionar(entidade)
        grupos.append(novo)
        print(f"Objeto {entidade} iniciado como centro do Cluster 1")
    elif qtd_total == 2:
        novo = Agrupamento(2)
        novo.adicionar(entidade)
        grupos.append(novo)
        print(f"Objeto {entidade} iniciado como centro do Cluster 2")
    else:
        grupo_vazio = next((g for g in grupos if not g.elementos), None)
        if grupo_vazio:
            grupo_vazio.adicionar(entidade)
            print(f"{entidade} alocado ao Cluster {grupo_vazio.id} (cluster reutilizado). Novo centroide: {[round(c, 2) for c in grupo_vazio.centroide]}")
        else:
            distancias = [calcular_distancia(entidade.vetor(), g.centroide) for g in grupos]
            menor_dist = min(distancias)
            indice = distancias.index(menor_dist)
            if menor_dist > max_dist and len(grupos) < 3:
                novo = Agrupamento(len(grupos) + 1)
                novo.adicionar(entidade)
                grupos.append(novo)
                print(f"{entidade} criou o Cluster {novo.id} (distância {menor_dist:.2f} > limite {max_dist})")
            else:
                grupos[indice].adicionar(entidade)
                print(f"{entidade} alocado ao Cluster {grupos[indice].id}. Novo centro: {[round(c, 2) for c in grupos[indice].centroide]}")

def iniciar_cadastro():
    limite_dist = 0
    grupos = []
    registros = []
    registros_cat = []

    while True:
        escolha = menu_opcao()
        
        if escolha == '1':
            limpar_tela_terminal()
            if limite_dist == 0:
                limite_dist = float(input("Informe o limite máximo de distância (ex: 2.5): ").strip())

            dados = input("Digite: Nome Idade Falta Nota (ex: Ana 20 0.1 7.5): ").strip()
            try:
                nome, idade, falta, nota = dados.split()
                pessoa = Pessoa(nome, float(idade), float(falta), float(nota))
                registros.append(pessoa)
                alocar_em_cluster(pessoa, grupos, limite_dist)
                mostrar_clusters(grupos)
            except Exception as erro:
                print(f"Erro ao cadastrar! {erro}. Verifique os dados.")

        elif escolha == '2':
            nome_alvo = input("Informe o nome a ser removido: ").strip()
            achou = False
            for grupo in grupos[:]:
                for item in list(grupo.elementos):
                    if hasattr(item, 'nome') and item.nome.lower() == nome_alvo.lower():
                        grupo.remover(item)
                        registros.remove(item)
                        print(f"{nome_alvo} excluído do Cluster {grupo.id}.")
                        if not grupo.elementos:
                            grupos.remove(grupo)
                        achou = True
                        break
                if achou:
                    break
            if not achou:
                print(f"{nome_alvo} não localizado.")
            mostrar_clusters(grupos)

        elif escolha == '3':
            nome_editar = input("Nome do aluno a editar: ").strip()
            idade_nova = ler_float("Nova idade (Enter para manter): ")
            falta_nova = ler_float("Nova %falta (Enter para manter): ")
            nota_nova = ler_float("Nova nota (Enter para manter): ")
            for grupo in grupos:
                for item in list(grupo.elementos):
                    if hasattr(item, 'nome') and item.nome.lower() == nome_editar.lower():
                        if idade_nova is not None:
                            item.idade = idade_nova
                        if falta_nova is not None:
                            item.falta = falta_nova
                        if nota_nova is not None:
                            item.nota = nota_nova
                        grupo.remover(item)
                        alocar_em_cluster(item, grupos, limite_dist)
                        print(f"{nome_editar} atualizado e realocado.")
                        break
                else:
                    continue
                break
            else:
                print(f"{nome_editar} não localizado.")
            mostrar_clusters(grupos)

        elif escolha == '4':
            limpar_tela_terminal()
            entrada = input("Informe um valor categórico (ex: Azul): ").strip()
            if not entrada.isalpha():
                print("Apenas palavras (sem números ou espaços) são aceitas.")
                continue
            if entrada not in mapeamento_strings:
                mapeamento_strings[entrada] = len(mapeamento_strings)
            categ = Categoria(entrada)
            categ.valor_num = mapeamento_strings[entrada]
            registros_cat.append(categ)
            alocar_em_cluster(categ, grupos, limite_dist)
            print("\nMapeamento atual de categorias:")
            for chave, val in mapeamento_strings.items():
                print(f"  {chave} -> {val}")
            mostrar_clusters(grupos)

        elif escolha == '5':
            limpar_tela_terminal()
            print("\nEncerrando cadastro. Estado final dos grupos:")
            mostrar_clusters(grupos)
            return grupos, registros + registros_cat
        else:
            print("Escolha inválida. Tente outra opção.")