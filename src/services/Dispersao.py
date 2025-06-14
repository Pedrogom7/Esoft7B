from src.models.cluster import distancia_euclidiana

def avaliar_dispersao(grupos, tolerancia, tamanho_min_cluster=1):
    registros_a_relocar = {}

    for grupo in grupos:
        registros_a_relocar[grupo.id] = []

    for grupo in grupos:
        for item in list(grupo.elementos):
            distancia_atual = distancia_euclidiana(item.vetor(), grupo.centroide)
            if distancia_atual > tolerancia:
                destino_mais_proximo = None
                menor_dist = float('inf')
                for outro in grupos:
                    if outro != grupo:
                        dist_temp = distancia_euclidiana(item.vetor(), outro.centroide)
                        if dist_temp < menor_dist:
                            destino_mais_proximo = outro
                            menor_dist = dist_temp
                if menor_dist < distancia_atual:
                    registros_a_relocar[grupo.id].append(item)
                    print(f"Elemento {item.nome} será removido do Grupo {grupo.id} (dist {distancia_atual:.2f}) e é mais próximo do Grupo {destino_mais_proximo.id} (dist {menor_dist:.2f})")

    criados = []
    for grupo_id, removidos in registros_a_relocar.items():
        if len(removidos) >= tamanho_min_cluster:
            novo = type(grupos[0])(len(grupos) + len(criados) + 1)
            original = next(g for g in grupos if g.id == grupo_id)
            for registro in removidos:
                original.remover(registro)
                novo.adicionar(registro)
            criados.append(novo)

    if criados:
        grupos.extend(criados)
        print(f"\n{len(criados)} novo(s) grupo(s) criado(s) com base na análise de dispersão.")
    else:
        print("\nNenhum grupo adicional gerado após avaliação.")

    for g in grupos:
        g.atualizar_centroide()