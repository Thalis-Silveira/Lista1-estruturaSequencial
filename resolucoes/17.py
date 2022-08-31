metros = float(input("Tamanho em m²: "))
#tinta = 1l para cada 6 metros


latas = (metros / 18 + metros // 18) // 6
galoes = (metros / 3.6 + metros // 3.6) // 6
valorLatas = 80 * latas
valorGaloes = 25 * galoes

galoesLatas = latas + galoes

print("Serão necessário {} latas, com o preço total de R${} ou de {} galões com o preço de R${}".format(latas, valorLatas,galoes,valorGaloes))
