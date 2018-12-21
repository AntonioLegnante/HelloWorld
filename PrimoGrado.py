#Equazione di primo grado
#Adesso ha senso usare a e b come variabile
a=int (input("Inserisci a "))
b=int (input("Inserisci b "))
if a==0 and b==0 :
			print ("l'equazione e' indeterminato,infinite soluzioni")
elif a==0 :
		print ("l'equazione e' impossibile,nessuna soluzione")
else :
	print ("l'incognita e' ", b/a)