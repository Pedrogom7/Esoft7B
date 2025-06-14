import os as sistema_operacional

def apagar_console():
    comando = 'cls' if sistema_operacional.name == 'nt' else 'clear'
    sistema_operacional.system(comando) 