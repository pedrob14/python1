largura: float = float(input('Qual a largura do cômodo? '))
profundidade: float = float(input('Qual a profundidade do cômodo?'))
altura: float = 2.9

area_paredes: float = 2 * (largura + profundidade) * altura

print("A area das paredes é", area_paredes)

area_teto: float = largura * profundidade

print(
    'A area do teto é:',
    area_teto

)

print('A litragem de tinta necesária é:',
      (area_paredes + area_teto) / 10
      )