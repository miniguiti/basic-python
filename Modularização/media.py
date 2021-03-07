'''
#Biblioteca que tem funções prontas
from statistics import *
def media(lista):
	return mean(lista)

def mediana(lista):
	return median(lista)

def moda(lista):
	return mode(lista)
'''

	#Calculando na mão (modo dificil):

# Soma dos n° / por qtd de elementos
def media(lista):
	media = sum(lista)/float(len(lista))
	return media

# N° no meio da lista ordenada 
def mediana(lista):
	lista_ordenada = sorted(lista)
	t = len(lista_ordenada)

	if t % 2 == 0:
		mediana = (lista_ordenada[int(t/2)] + lista_ordenada[int((t/2)-1)])/2 
	elif t % 2 == 1:
		mediana = lista_ordenada[int((t/2) + 0.5)]

	return mediana	


# N° que mais se repete
def moda(lista):
	lista_dic = {}
	for l in lista:
		if l not in lista_dic:
			lista_dic[l] = 1
		else:
			lista_dic[l] += 1

	maior_repeticao = max(lista_dic.values())

	for i in lista_dic:
		if lista_dic[i] == maior_repeticao:
			moda = i 

	return moda