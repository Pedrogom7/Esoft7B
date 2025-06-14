from src.controllers.cadastro_controller import realizar_cadastro
from src.controllers.cluster_controller import realizar_clusterizacao
from src.utils.limpar_tela import limpar_tela as limpar_terminal

def executar_programa():
    limpar_terminal()
    print("=== Sistema Dinâmico de Clusterização K-means ===")
    
    agrupamentos, registros = realizar_cadastro()
    realizar_clusterizacao(agrupamentos, registros)

if __name__ == "__main__":
    try:
        executar_programa()
    except KeyboardInterrupt:
        print("\nProcesso interrompido pelo usuário. Até breve!")