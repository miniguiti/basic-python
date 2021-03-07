#Dicionarios não possuem indice, ou seja, é idetificado por sua chave
meu_dicionario = {"A":"AMEIXA", "B": "BOLA", "C": "CACHORRO"}

#Exibindo por chave
print(meu_dicionario["A"])

#Exibindo
for chave in meu_dicionario:
	print(chave + ":" +  meu_dicionario[chave])


# EXIBIBINDO COM FUNÇÕES:

#Exibe chaves 
for chave in meu_dicionario.keys():
	print(i)

#Exibe tupla (chave e valores)
for chave in meu_dicionario.items():
	print(i)

#Exibe valores
for chave in meu_dicionario.values():
	print(i)