'''
def cerdo(x):
	Fl = x[0]
	if Fl in "aeiou":
		cosa = x+"ay"
	else:
		cosa = x[1:]+Fl+"ay"
	return cosa
print(cerdo("Word"))
'''
'''
def nombre(x):
	print(f"Hola {x}")
nombre('Juan')
'''
'''
def par(x):
	if x%2==0:
		return True
	else:
		return False

if par(2) == True:
	print("Esta madre es par")
'''
def low (a,b):
	if a>b:
		return True
	elif b<a:
		return False




