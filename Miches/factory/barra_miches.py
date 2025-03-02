class BarraMiches:
    @staticmethod
    def prepararMichelada(method, miche):
        if method == "kitichela":
            from miches.kitichela import Kittychela
            return Kittychela(miche)

        elif method == "botachela":
            from miches.botachela import Botachela
            return Botachela(miche)

        elif method == "gomichela":
            from miches.gomichela import Gomichela
            return Gomichela(miche)

        else:
            raise ValueError("Tipo de michelada no existente")