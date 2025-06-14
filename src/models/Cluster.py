import math
from src.models.elemento import Elemento

def calcular_distancia(v1, v2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(v1, v2)))

class Agrupamento:
    def __init__(self, identificador):
        self.identificador = identificador
        self.itens = []
        self.representante = None

    def incluir(self, item):
        self.itens.append(item)
        self.recalcular_representante()

    def excluir(self, item):
        self.itens.remove(item)
        self.recalcular_representante()

    def modificar_item(self, nome, idade_nova=None, falta_nova=None, nota_nova=None):
        for obj in self.itens:
            if obj.nome.lower() == nome.lower():
                if idade_nova is not None:
                    obj.idade = idade_nova
                if falta_nova is not None:
                    obj.falta = falta_nova
                if nota_nova is not None:
                    obj.nota = nota_nova
                self.recalcular_representante()
                return True
        return False

    def recalcular_representante(self):
        if not self.itens:
            self.representante = None
            return
        for obj in self.itens:
            obj.is_centroide = False
        acumulado = [0, 0, 0]
        for obj in self.itens:
            vetor = obj.vetor()
            for i in range(3):
                acumulado[i] += vetor[i]
        total = len(self.itens)
        media = [valor / total for valor in acumulado]
        self.representante = media
        mais_perto = min(self.itens, key=lambda i: calcular_distancia(i.vetor(), media))
        mais_perto.is_centroide = True

    def __repr__(self):
        conteudo = "\n  ".join(str(i) for i in self.itens)
        return f"Agrupamento {self.identificador} - Representante: {self.representante}\nItens:\n  {conteudo}"