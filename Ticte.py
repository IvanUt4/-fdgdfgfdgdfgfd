madres = "123456789"
while madres != "":

	pos = int(input("Ingrese un numero "))
	ver = str(pos) in madres
	if ver == True:
		madres = madres.replace(str(pos),"")
		print(madres)
		print(ver)
	else:
		print("Waton y la reconcha de tu madre, eres un completo pendejo")
