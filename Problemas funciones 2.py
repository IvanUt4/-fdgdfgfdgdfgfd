
def contador(cosa):
	men = 0
	may = 0
	for i in cosa:
		if i in "qwertyuiopasdfghjklzxcvbnm":
			men += 1
		if i in "QWERTYUIOPASDFGHJKLZXCVBNM":
			may += 1 
	return(f"El numero de palabras en mayusculas es {may} y el numero de minisculas es {men}")



import string
letras = string.ascii_lowercase
def todos(str):
	global letras
	for i in str.lower():
		letras = letras.replace(i,"")
		print(letras)
	return letras == ""

print(todos("The quick brown fox jumps over the lazy dog"))
print(letras)

import math as ma
def sp(r):
	return 4/3*(ma.pi*(r**3))
