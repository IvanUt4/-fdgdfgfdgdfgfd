import os
def draw (madre):
	restos = "123456789"
	j1 = ""
	j2 = ""
	es = True
	turn = 0
	while es == True:
		j1 = str(input("El jugador 1 quiere utlizar las X o O? "))
		j1 = j1.upper()
		if j1 == "X":
			break
		if j1 == "O":
			break

	if (j1 == "X"):
		j2 = "O" 
	elif (j1 == "O"):
		j2 = "X"


	while restos != "":
		
		pos = int(input("Ingrese la posicion que quiere tomar "))
		if (str(pos) in restos) == True:
			
			restos = restos.replace(str(pos),"")
			if turn %2 == 0:
				madre[pos] = j1
			if turn %2 != 0:
				madre[pos] = j2
				
			os.system('cls')
			print(madre[7]+"|"+madre[8]+"|"+madre[9])
			print("-----")
			print(madre[4]+"|"+madre[5]+"|"+madre[6])
			print("-----")
			print(madre[1]+"|"+madre[2]+"|"+madre[3])
			turn += 1
			if (madre[1] == j1 and madre[2] == j1 and madre[3] == j1) or (madre[1] == j1 and madre[5] == j1 and madre[9] == j1) or (madre[1] == j1 and madre[4] == j1 and madre[7] == j1) or (madre[4] == j1 and madre[5] == j1 and madre[6] == j1) or (madre[7] == j1 and madre[8] == j1 and madre[9] == j1) or (madre[7] == j1 and madre[5] == j1 and madre[3] == j1)  or (madre[8] == j1 and madre[5] == j1 and madre[2] == j1) or (madre[9] == j1 and madre[6] == j1 and madre[3] == j1):
				print("Gana jugador 1")
				break
			if (madre[1] == j2 and madre[2] == j2 and madre[3] == j2) or (madre[1] == j2 and madre[5] == j2 and madre[9] == j2) or (madre[1] == j2 and madre[4] == j2 and madre[7] == j2) or (madre[4] == j2 and madre[5] == j2 and madre[6] == j2) or (madre[7] == j2 and madre[8] == j2 and madre[9] == j2) or (madre[7] == j2 and madre[5] == j2 and madre[3] == j2)  or (madre[8] == j2 and madre[5] == j2 and madre[2] == j2) or (madre[9] == j2 and madre[6] == j2 and madre[3] == j2):
				print("Gana jugador 2")
				break
		else:
			print("Esa posicion esta tomada, elija otra.")
		
test  = ["xD"," "," "," "," "," "," "," "," "," "]

 
draw(test)