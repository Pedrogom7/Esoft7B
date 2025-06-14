from src.models.cluster import Cluster, distancia_euclidiana

def agrupamento_k_sequencial(registros):
    grupos = []

    grupo_a = Cluster(1)
    grupo_a.adicionar(registros[0])
    grupos.append(grupo_a)
    print(f"Instância {registros[0]} definida como centroide do Grupo 1")

    grupo_b = Cluster(2)
    grupo_b.adicionar(registros[1])
    grupos.append(grupo_b)
    print(f"Instância {registros[1]} definida como centroide do Grupo 2")

    for registro in registros[2:]:
        dist_por_grupo = [distancia_euclidiana(registro.vetor(), grupo.centroide) for grupo in grupos]
        indice_mais_proximo = dist_por_grupo.index(min(dist_por_grupo))
        grupos[indice_mais_proximo].adicionar(registro)
        novo_centroide = [round(valor, 2) for valor in grupos[indice_mais_proximo].centroide]
        print(f"Instância {registro} atribuída ao Grupo {grupos[indice_mais_proximo].id}. Novo centroide: {novo_centroide}")

    return grupos