from factory.barra_miches import BarraMiches
from station.station import Miche

miches=[
    Miche("Michelada 1"),
    Miche("Michelada 2"),
    Miche("Michelada 3")
]

tipos = ["kitichela", "botachela", "gomichela"]
for i in range(len(miches)):
    miche_instance = BarraMiches.prepararMichelada(tipos[i], miches[i])
    print(f"Preparando una {tipos[i]} para la {miches[i].michelada}")
    print(f"Total cost: ${miches[i].calculate_total_cost(miche_instance)}\n")



