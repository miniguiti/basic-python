
#Abrindo arquivo
arquivo = open("arquivo.txt")
linhas = arquivo.readlines()

#Criando arquivo
w = open("arquivotxt2.txt", "w")

w.write("Esse eh meu arquivo")

w.close()