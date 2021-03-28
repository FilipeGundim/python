nome=input("digite um nome: ")
idade = int(input("digite a idade: "))
doencaGrave = input("é doença grave? ").upper()

if idade >= 65:
    print(nome + " é prioritário")
elif doencaGrave == 'SIM':
    print(nome + " tem prioridade")
else:
    print(nome + " não é prioritário")

print("fim")
