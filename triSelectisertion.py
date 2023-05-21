import random 

def tri_selection(tableau):
    nb = len(tableau)
    for en_cours in range(0,nb-1):    
        plus_petit = en_cours
        for j in range(en_cours+1,nb) :
            if tableau[j] < tableau[plus_petit] :
                plus_petit = j
        if min is not en_cours :
            temp = tableau[en_cours]
            tableau[en_cours] = tableau[plus_petit]
            tableau[plus_petit] = temp

def plus_petit(tableau):
    indice_petit = 0
    for i in range(1, len(tableau)):
        if tableau[i] < tableau[indice_petit]:
            indice_petit = i          
    return indice_petit


tab = [random.randint(0,20) for i in range(10)]
tab1 = [12]
print (plus_petit(tab1))
print(tab)
tri_selection(tab)
print(tab)