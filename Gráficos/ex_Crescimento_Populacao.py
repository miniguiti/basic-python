#Crescimento da População Brasileira  1980-2016
# DataSus: origem dos dados

dados = open("populacao-brasileira.csv").readline()

x = []
y = []

for i in range(len(dados)):
	if i != 0:
		linha = dados[i].split(";")
		x.append(linha[0])
		y.append(linha[1])