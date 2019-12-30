'''
list = "Mokou"
name = []
for i in list:
	name.append(i)
for x in name:
	print(x)
name2 = [x for x in list]
for t in name2:
	print(t)
	'''
lista = [x for x in range(0,11) if x%2==0]
C = [0,10,20,34.5]
F = [((num*9/5)+32) for num in C ]	
for q in F:
	print (q)