x = 50
def fun():
	global x
	print(f"Esta madre es {x}")
	x += 50
	print(f"Ahora es {x}")
fun()
print(f"Esta es la parte de fuera {x}") 