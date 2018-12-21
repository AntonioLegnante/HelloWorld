#Scegliere se calcolare il volume di un Cubo o di una Sfera
import math
Scelta=int (input ("1 - Cubo, 2 - Sfera "))
if Scelta==1:
		Lato=int (input ("Inserisci il lato "))
		print ("Il volume è ", Lato**3)
elif Scelta==2 :
		Raggio=int (input ("Inserisci il Raggio "))
		print ("Il volume è ", 4/3*math.pi*Raggio**3)
else :
	print("Sai leggere?")