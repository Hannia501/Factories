from miches.michelada_tradicional import MicheladaTradicional

class Botachela(MicheladaTradicional):
    def costoExtra(self):
        return 20

    def preparar(self):
        print(f"Preparando una Botachela con {self.miche.tipo}")

