from difflib import SequenceMatcher

print("Detector de plagio")
print("inserte el primer texto")
file1 = input()
print("------------------------------")
print("Ahora inserte el segundo texto")
file2 = input()

with open("1.txt") as file3:

	fil1data=file1
	file2data=file2
	similarity=SequenceMatcher(None, fil1data,file2data).ratio()

	print ("----------------------------")
	print("El porcentaje de plagio es de un:")
	print(similarity*100)

	exit