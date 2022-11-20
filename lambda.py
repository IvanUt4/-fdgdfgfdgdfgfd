sq = lambda num: num**2
lista = [1,2,3,4,5]
lista2 = ["Mokou","Yukari","Katakuri"]

letra  = str(input("Ingrese la letra que quiere analizar  "))
letra =letra.lower()
print(sq)
print(list(filter(lambda num: num%2 == 0,lista)))
print(list(filter(lambda st: (st[0].lower() == letra),lista2)))