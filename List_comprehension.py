#List comprenhension

# Exibindo o quadrado de uma lista 
x = [1,2,3,4,5]
y = []

for i in x:
	y.append(i**2)

print(x)
print(y)
  

#Agora com List Comprehension

#Sintax x = [valor_a_adicionar laco condicao]

print("Exemplo sem condicao") 
x = [1,2,3,4,5]
y = [i**2 for i in x]

print(x)
print(y)


print("Exemplo com condicao")
x = [1,2,3,4,5]
y = [i**2 for i in x]
z = [i for i in x if i%2==1]
print(x)
print(y)
print(z)
