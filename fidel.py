import random
c=True
n=0
score=100
nbr=random.randint(1,100)
while c==True:
    x=int(input("Entrer un nombre:"))
    if x<nbr:
        print("le nombre entre est trop petit :")
        n+=1
        score-=5
    elif x>nbr:
        print("le nombre entre est trop grand :")
        n+=1
        score-=5
    else :
        print("FELICITATION!!!")
        n+=1
        print(f"you find the gost number on the {n} attempt. ")
        c=False
print("End!!!")

    
    
    




