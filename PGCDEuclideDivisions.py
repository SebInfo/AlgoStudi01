# Calcul du PGCD algo Euclide 300 av J.C.
a=eval(input("Valeur de a ?")) 
b=eval(input("Valeur de b ?")) 
# On change les valeurs si besoin pour que a >= b
if ( b > a ):
   a, b = b, a

reste = a%b
while(reste != 0):
   a = b
   b = reste
   print ("a : ", a)
   print ("b : ", b)
   print ("reste : ", reste)
   reste = a%b
   
print(b) # Le PGCD est trouvé
