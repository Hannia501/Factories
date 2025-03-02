from miches.michelada_tradicional import MicheladaTradicional
class Kittychela(MicheladaTradicional):
    def costoExtra(self):
        return  15

    def preparar(self):
        print(f"Preparando una Kittychela con {self.miche.tipo}")