metros = float(input("Tamanho em m²: "))
#tinta = 1l para cada 3 metros/venda em lata de 18 l = R$80 ---> informar quantidade de latas e valor

latas = (metros / 18 + metros // 18) // 3
valor = 80 * latas

print("Serão necessário {} latas, com o preço total de R${}".format(latas, valor))
