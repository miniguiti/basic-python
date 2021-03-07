# Zip: Compacta as duas listas como se fosse 1 para percorrer usando laço

lista1 = [1,2,3,4,5]
lista2 = ["abacate","bola","cachorro","dinheiro","elefante"]
lista3 = ["R$ 2,00", "R$ 4,00", "R$ 0,00", "Nao tem preco", "R$ 2,00"]

for numero, nome, preco in zip(lista1,lista2, lista3):
	print(numero, nome, preco)
