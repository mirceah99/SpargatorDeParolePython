#Spargatorul de parole 
#snapchat

import time
nrMindDeCaractere = 6
litere = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
f = open("Parola.txt","r")
parola_cauta = f.readline()

parola = [0]*nrMindDeCaractere
def listToString(lista):
    parolaString = ""
    for elem in lista:
        parolaString = parolaString + litere[elem]
    return parolaString
def incrementParola(parola):
    for i in range (len(parola)-1,-1,-1):
        if (parola[i] != len(litere)-1):
            parola[i] = parola[i] + 1
            return parola
        if(parola[i] == len(litere)-1 and parola[i-1] != len(litere)-1 ):
            for j in range (i,len(parola),1):
                parola[j] = 0
            parola[i-1] = parola[i-1] + 1
            return parola


while (parola_cauta != listToString(parola)):
    incrementParola(parola)
    #print(listToString(parola))
    if(parola == [len(litere)-1]*len(parola)):
        parola.insert(0, 0)
f2 = open ("Raspuns.txt", "w")
f2.write(listToString(parola))

print("AM TERMINAT! ")
