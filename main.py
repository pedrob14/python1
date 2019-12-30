from calculadora import Calculadora

calc = Calculadora()

largura: float = float(input('Qual a largura do cômodo? '))
profundidade: float = float(input('Qual a profundidade do cômodo?'))
altura: float = 2.9

print("A area das paredes é",
      calc.calcular_area_paredes(largura, profundidade, altura))



print(
    'A area do teto é:',
    calc.calcular_area_teto(largura, profundidade)
)

print('A litragem de tinta necesária é:',
      calc.calcular_litragem_necessaria()
      )