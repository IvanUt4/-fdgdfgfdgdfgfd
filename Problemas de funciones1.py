'''
def menor (a,b):
	if a>b:
		return b
	elif b>a:
		return a
	else:
		return "estas madres son iguales"
print(menor(5,4))
'''
'''
def iguales (*cosas):
	bol = True
	palabra = cosas[0]
	letra = palabra[0].lower()
	for i in cosas:
		if i[0].lower() == letra:
			bol = True
		elif i[0].lower() != letra:
			bol = False
			break
	return bol
print(iguales("Mono","mantis","Mlefante"))
'''
'''
def suma(*numeros):
	if sum(numeros) == 20:
		return True
	else:
		return False
print(suma(10,1))
'''
'''
def reversa(tex):
	
	lista = (tex).split()
	reg = ""
	for i in reversed(lista):
		reg = reg + " " +i
	return reg
'''
'''
def tres (*arg):
	com = 0
	for i in arg:
		if i == 3 and com != 2:
			com += 1
		elif i!=3:
			com = 1
		elif com == 2:
			return True
			break
	return False

print(tres(3,0,3,3,0,1,2,3,4))
'''
'''
def triple(s):
	ret = []
	res = s.split()
	ora = ""
	for i in s:
		pal = i
		ret.append([pal]*3)
	for i in ret:
		for j in i:
			ora += j
	return ora 
print(triple("Fujiwara no"))
'''
'''
def triple(s):
	ret = ""
	for i in s:
		ret += i*3
	return ret
print(triple("Fujiwara no mokou"))
'''
'''
def james(*str):
	con = 0
	ret = False
	for i in str:
		if con == 0  and i == 0:
			con += 1
		elif con ==1 and i == 0:
			con += 1
		elif con == 2 and i == 7:
			return True 
			break
	return False
print(james(7,0,6,7))
'''
def suma6(*args):
	suma = True
	To = 0
	for i in args:
		if i == 6:
			suma = False
		elif i == 9:
			suma = True
		elif suma == True:
			To += i
	return To
print(suma6(1,2,3,6,1,9)) 









