tabuada=int(input("digite um nuemro: "))
print("gerando tabuada do numero ", tabuada)

for valor in range(1, 11, 1):
    print(str(tabuada) + " x " + str(valor) + "=" + str((tabuada*valor)))