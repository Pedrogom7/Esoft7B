class Registro:
    def __init__(self, identificador, idade_valor, percentual_faltas, nota_final):
        self.identificador = identificador
        self.idade_valor = idade_valor
        self.percentual_faltas = percentual_faltas
        self.nota_final = nota_final
        self.eh_centroide = False

    def para_vetor(self):
        return [self.idade_valor, self.percentual_faltas, self.nota_final]

    def __repr__(self):
        marcador = " (Centroide)" if self.eh_centroide else ""
        return f"{self.identificador}: [{self.idade_valor}, {self.percentual_faltas}, {self.nota_final}]{marcador}"