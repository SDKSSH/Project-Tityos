doigdrip = ""

def lireFichier():
    '''
    Lis le fichier ascii du doigdrip et le met dans la variable global :D
    '''
    global doigdrip
    f = open("./easteregg/ascii/doigdrip.txt", "r", encoding="utf-8")
    l = f.readline()
    while(l != ""):
        doigdrip = doigdrip+l
        l = f.readline()
    f.close()


def AfficherDoigby():
    '''
    Affiche le dieu, le tous puissant, DOIGBY !!!!!!
    '''
    global doigdrip
    print(doigdrip)
