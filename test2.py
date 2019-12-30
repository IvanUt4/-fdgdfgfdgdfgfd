texto = "Suwako Mokou Sumireko"
lista = texto.split()
for i in lista:
	if i[0]=="S":
		print(i)
print("\n")
div3 = [x for x in range(1,51) if x%3 == 0]
for r in div3:
	print(r)
print("\n")
lista2 = [1,2,3]
if len(lista2)%2 == 0:
	print("Los espacios de la lista son pares")
else:
	print("Es impar")