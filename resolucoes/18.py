tamanho = int(input("Escreva o tamanho do arquivo(MB): "))
velocidade = int(input("Escreva a velocidade do link(Mbps): "))

mb = velocidade/8
tempo = (tamanho / mb) / 100
print("levara cerca de {} minutos".format(tempo))