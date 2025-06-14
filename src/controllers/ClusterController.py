from src.models.cluster import Cluster as Agrupamento
from src.services.kmeans import k_means_sequencial as executar_kmeans
from src.services.dispersao import analisar_dispersao as verificar_dispersao

def aplicar_clusterizacao(grupos, dados):
    if len(dados) < 2:
        print("São necessários ao menos dois registros para iniciar a clusterização.")
        return

    executar_kmeans(dados)
    limite_padrao = 2.5
    verificar_dispersao(grupos, limite_padrao)