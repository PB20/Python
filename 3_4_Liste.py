x = open("/home/swt/Schreibtisch/Klammercode.txt", "r") 
Code=str(x.read()) 

Fehler=0;   Kl1=[];   Kl2=[] #Fehlerart & Klammerarrays initialisieren  
for Pos in range(len(Code)): 
    if Code[Pos]=='{': 
        Kl1.append(Pos) #Werte mithilfe von .append .insert & .pop hinzufügen/löschen
    elif Code[Pos]=='}': 
        if len(Kl1)>0:
            Kl1.pop(len(Kl1)-1)         
        else:
            Fehler=3
            break
    elif Code[Pos]=='(': 
        Kl2.append(Pos)
    elif Code[Pos]==')': 
        if len(Kl2)>0:
            Kl2.pop(len(Kl2)-1)
        else:
            Fehler=4
            break         

if len(Kl1) > 0:
    Fehler=1
elif len(Kl2) > 0:
    Fehler=2

def SpalteZeile (Pos): 
    Zeile=1 
    for i in range(Pos):  
        if Code[i]=='\n':  
            Zeile+=1  
            Pos_letzt=i  
    Spalte=Pos-Pos_letzt 
    return Spalte, Zeile 

Zeile=1 # Zeilenvariable initialisieren
if Fehler==1:
    Spalte,Zeile=SpalteZeile(Kl1[0])     
    print(f'Anzahl überschüssiger offener geschweifter Klammern:{len(Kl1)},\ndie erste befindet sich in Zeile:{Zeile} , Spalte:{Spalte}') 
elif Fehler==2:
    Spalte,Zeile=SpalteZeile(Kl2[0])        
    print(f'Anzahl überschüssiger offener runder Klammern:{len(Kl2)},\ndie erste befindet sich in Zeile:{Zeile} , Spalte:{Spalte}')     
elif Fehler==3:
    Spalte,Zeile=SpalteZeile(Pos)         
    print(f'geschlossene geschweifte Klammer zu viel in Zeile:{Zeile} , Spalte:{Spalte}')
elif Fehler==4:
    Spalte,Zeile=SpalteZeile(Pos)
    print(f'geschlossene runde Klammer zu viel in Zeile:{Zeile} , Spalte:{Spalte}')
else:
    print('Keine Klammerfehler entdeckt')