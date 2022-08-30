salarioPorHora = float(input("Digite o seu sálario por hora: "))
horaTrabalhada = int(input("Digite o numero de horas trabalhadas: "))

totalMes = salarioPorHora * horaTrabalhada

print("Você possui um salario de R$ {:.2f} por hora\ntrabalhou {:.2f} horas\nSendo assim seu sálario mensal é de R${:.2f}".format(salarioPorHora,horaTrabalhada,totalMes))