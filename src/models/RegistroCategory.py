class RegistroCateg:
    def __init__(self, rotulo_texto):
        self.rotulo_texto = rotulo_texto
        self.valor_numerico = None
        self.eh_centroide = False

    def para_vetor(self):
        return [self.valor_numerico, 0, 0]

    def __repr__(self):
        marcador = " (Centroide)" if self.eh_centroide else ""
        return f"{self.rotulo_texto}: [{self.valor_numerico}]{marcador}"