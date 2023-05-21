# Calcul d'un PGCD par différences successives 
a=eval(input("Valeur de a ?")) 
b=eval(input("Valeur de b ?")) 
while (a!=b): 
    d=(a-b) 
    a=max(d,b) 
    b=min(d,b) 
print("pgcd=",d) 
if d==1: 
    print("Les deux entiers sont premiers entre eux.") 