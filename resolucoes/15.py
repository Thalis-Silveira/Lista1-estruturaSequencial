salarioPorHora = float(input("Quanto você ganha por hora: "))
numeroHorasMes = int(input("Numero pde horas no mês: "))

total = salarioPorHora * numeroHorasMes


impostoRenda = total * 0.11
inss = total * 0.08
sindicato = total * 0.05

SalarioLiquido = total - (impostoRenda + inss + sindicato)

print("+Sálario bruto: R${:.2f}\n-IR(11%): R${:.2f}\n-INSS(8%):R${:.2f}\n-sindicato(5%):R${:.2f}\n=Salário Liquido: R${:.2f}".format(total,impostoRenda,inss,sindicato,SalarioLiquido))