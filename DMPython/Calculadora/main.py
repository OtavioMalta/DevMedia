from calculadora import Calculadora
from comodo import Comodo


calc = Calculadora()

comodo = Comodo(
        input("Qual a largura do comodo? "),
        input("Qual a profundidade do cômodo? ")
)

print("A area das parede é: ",
        calc.calcular_area_paredes(comodo)
)

print("A area do teto é: ",
        calc.calcular_area_teto(comodo)
)

print("A litragem de tinta necessaria é: ", 
        (calc.calcular_litragem())
)