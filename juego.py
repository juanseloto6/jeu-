import random

vies = 0

while 1:
    try:
        dificulte = str(input('choisissez la dificulté du jeu : facile , moyenne  , difficile: '))
        if dificulte not in ['facile', 'moyenne', 'difficile']:
            raise ValueError
        else:
            break
    except ValueError:
        print("vous devez seulement mettre soit facile soit moyenne soit difficile")
        continue

if dificulte == "facile":
    print('le nombre de vies est 20')
    vies = 20
elif dificulte == "moyenne":
    print('le nombre de vies est 10 ')
    vies = 10
elif dificulte == "difficile":
    print("le nombre de vies es 5")
    vies = 5

# ceci sert pour avoir un numero au hazard
numero_random = random.randint(1, 100)
print('ce jeu consiste à deviner un numero entre 1 et 100 inclus ')

while vies >= 1:

    while 1:
        try:
            numero = int(input("mettez un numero entre 1 et 100 : "))
            if 0 > numero > 100:
                vies=vies
                raise ValueError
            else:
                break
        except ValueError:
            print('vous devez seulement mettre des numeros entre 1 et 100 inclus , essayez à nouveau ')
            vies=vies
            continue

    if numero_random < numero:
        vies -= 1
        print('votre numero de vies est égal à', vies)
        print('une piste : mettez une valeur plus petite')

    if numero_random > numero:
        vies -= 1
        print('votre numero de vies est égal à ', vies)
        print('une piste : mettez une valuer plus grande  ')

    if numero_random == numero:
        print("felicitations vous avez gagné!")
        break

if vies == 0:
    print('Vous avez plus de vies')

           
    
    
        
    

    
 
     
    