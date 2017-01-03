y = int(input("Digite seu Faturamento: R$ "))
x = 45000

faturamento = len(list(range(x,y,5000)))*10

print("O valor adicional para o seu plano é R$ %.2f" %float(faturamento))
