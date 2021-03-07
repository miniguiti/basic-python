#Função enumerate

print("Exibindo indice da lista")
lista = ["abacate","bola", "cachorro"]

for i in range(len(lista)):
	print(i, lista[i])


print("EXIBINDO DO JEITO PYTHONICO")

for i, nome in enumerate(lista):
	print(i, nome)