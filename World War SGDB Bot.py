
import random

participants = []
objectes = []
contador = 1
def readParticipants():
    global participants
    with open('participants.txt') as pa:
        for i in pa:
            participants.append(i[:-1])

def readObjects():
    global objectes
    with open('objectes.txt') as ob:
        for i in ob:
            objectes.append(i[:-1])

def randomChoices():
    global objectes,participants,contador
    while(len(participants)>1):
        batalla = random.sample(participants,2)  #funcio que pille dos elements diferents randoms de una llista
        print('Jornada ' + str(contador) + ' del SGDB War Bot')
        print('Senfronten ' + batalla[0] + ' vs ' + batalla[1])
        guanyador = random.choice(batalla)
        batalla.remove(guanyador)
        perdedor = batalla[0]
        print(guanyador+' ha matat a '+perdedor+' amb '+random.choice(objectes))
        participants.remove(perdedor)
        contador+=1
        print('')

    print('El guanyador de la primera SGDB War es: '+guanyador)

if __name__ == "__main__":
    print('')
    readParticipants()
    readObjects()
    randomChoices()
    