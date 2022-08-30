from tokenize import Double
from unicodedata import numeric


numInt =  int(input("Digite um numero inteiro: "))
NumInt2 = int(input("Digite um numero inteiro: "))
NumReal =  float(input("Digite um numero real: "))

ProdDobro = (2 * numInt) * (NumInt2/2)
SomaTriplo = (3 * numInt) + NumReal
Aocubo = NumReal ** 3

print("Produto do dobro do 1° com metade do 2°: {:.2f}\nA soma do triplo do 1° com o 3: {:.2f}\nO 3° elevado ao cubo {:.2f}".format(ProdDobro,SomaTriplo,Aocubo))