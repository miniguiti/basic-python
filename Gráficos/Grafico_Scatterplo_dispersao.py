# Visualizãção de dados em Python

import matplotlib.pyplot as plt 

x = [1,2,5,7,9]
y = [2,3,7,1,0]

titulo = "Grafico de Barras"
eixox = "Eixo X"
eixoy = "EixoY"

#Legendas
plt.title(titulo)
plt.ylabel(eixoy)
plt.xlabel(eixox)

plt.scatter(x,y, label="Meus pontos,", color='r')
plt.plot(x,y)
plt.legend()
  
plt.show()