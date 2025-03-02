
class Miche:
    def __init__(self, michelada):
        self.michelada = michelada
        self.costo = 40


    def calculate_total_cost(self,tipo):
        extra_cost = tipo.costoExtra()
        return self.costo + extra_cost
