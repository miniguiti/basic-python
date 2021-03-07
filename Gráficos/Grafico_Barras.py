# Visualizãção de dados em Python

import matplotlib.pyplot as plt 

#Grafico 1 
'''
x = [1,2,3,4,5]
y = [2,3,7,1,0]

titulo = "Grafico de Barras"
eixox = "Eixo X"
eixoy = "EixoY"

#titulo
plt.title("Titulo de um grafico maroto")

#Eixos
plt.xlabel("Eixos X")
plt.ylabel("Eixo Y")
plt.bar(x,y)
plt.show()
'''

#Grafico 2: compara 2 eixos

x1 = [1,2,5,7,9]
y1 = [2,3,7,1,0]

x2 = [2,4,6,8,10]
y2 = [5,1,3,7,4]

titulo = "Grafico de Barras"
eixox = "Eixo X"
eixoy = "EixoY"

#Legendas
plt.title(titulo)
plt.ylabel(eixoy)
plt.xlabel(eixox)

plt.bar(x1,y1, label = "Grupo 1")
plt.bar(x2,y2, label = "Grupo 2")
plt.le gend()

plt.show()