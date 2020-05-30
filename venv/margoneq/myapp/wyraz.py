def silnia(k):
	suma = 1
	for i in range(k):
		suma  += suma * i
	return suma
try:
	liczba = int(input("Wprowadź liczbę "))
except:
	print("Błędny input")
suma = 1
for i in range(len(str(liczba))):
	suma *= silnia(int(str(liczba)[i]))
if suma == liczba:
	print("Liczba "+ str(liczba)+ " jest równa sumie swojej silni ")
else:
	print("Liczba "+ str(liczba)+ " nie jest równa sumie swojej silni, lecz jest równa "+ str(suma))