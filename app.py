def offres(x) : 
    if x == 1 : 
      P = print("Abonnement mensuel : 200DH" , "Minutes gratuites et Coûte la minute : Illimité")
    if x == 2 :
      P = print("Abonnement mensuel : 100DH" , "Minutes gratuites : 2h " , "Coûte la minute : 0.5DH")
    if x == 3 :
      P = print("Abonnement mensuel : 50DH" , "Minutes gratuites : 1h " , "Coûte la minute : 1DH")
    if x == 4 :
      P = print("Abonnement mensuel : 20DH" , "Minutes gratuites : 30min " , "Coûte la minute : 1.5DH")
    if x == 5 :
      P = print("Abonnement mensuel : 0DH" , "Minutes gratuites : 0 " , "Coûte la minute : 2DH")
    if x<1 or x>5 : 
       P = print("il ya pas cette chiffre")
    return P 
x = int(input("entrez un chiffre de 1 à 5 : "))
print(offres(x))