#Hassan Ali El Gazouini
from itertools import product

def inspectar_arqui(arquivo):
  with open(arquivo, 'r') as f:
    linha = f.read().splitlines()

  
  primeira_operacao = int(linha[0])
  indice = 1

  for i in range(primeira_operacao):
  
    operacao = linha[indice].strip()
    conjA = set(linha[indice + 1].split(','))
    conjB = set(linha[indice + 2].split(','))
    indice += 3
    
    if operacao == 'U':
      print(f"Uniao: conjunto A {conjA}, conjunto B {conjB} Resultado:",conjA.union(conjB))
    elif operacao == 'I':
      print(f"Interseccao: conjunto A {conjA}, conjunto B {conjB}  Resultado:"
      ,conjA.intersection(conjB))
    elif operacao == 'D':
      print(f"Diferenca:  conjunto A {conjA}, conjunto B {conjB} Resultado:",conjA.difference(conjB))
    elif operacao == 'C':
      print(f"Produto cartesiano: conjunto A {conjA}, conjunto B {conjB} Resultado:",list(product(conjA, conjB)))
  

arquivo = 'data.txt'
inspectar_arqui(arquivo)
