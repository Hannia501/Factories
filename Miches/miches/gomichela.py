from miches.michelada_tradicional import MicheladaTradicional

class Gomichela(MicheladaTradicional):
    def costoExtra(self):
        return 12

    def preparar(self):
        print(f"Preparando una Gomichela con {self.miche.tipo}")
