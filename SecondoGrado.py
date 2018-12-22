#Equazioni di 2 Grado nella forma ax+bx+c=0
import math
a=int (input ("Inserisci a"))
b=int (input ("Inserisci b"))
c=int (input ("Inserisci c"))
if a==0 and b==0 and c==0:
    print ("L'equazione e' indeterminata,infinite soluzioni")
elif a==0 and b==0:
    print ("L'equazione e' impossibile,nessuna soluzione")
elif a==0:
    print ("l'incoglita e'", -c/b)
else:
    delta=b**2-4*a*c
    if delta<0:
        Rad_delta=math.sqrt(-delta)
        re= -b/ (2.0 * a)
        Val=Rad_delta/ (2.0 *a) #soluzione non capita e problemi con l'uso della funzione abs
	imm= abs(Val)
        print ("x1 =", re, "-i", imm)
        print ("x2 =", re, "+i", imm)
    elif delta==0:
        print ("2 soluzione reali e coincidenti")
        print ("x1=x2=",-b/ (2.0 *a))
    else:
        print ("2 soluzione reali e distinte")
        print ("x1=", -b-math.sqrt(delta)/a*2.0)
        print ("x2=", -b+math.sqrt(delta)/a*2.0)
	