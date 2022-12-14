import models.Player as Player
import os

texts = {}

def loadTexts():
    '''
    Lis tous les fichiers dans le dossiers texts et les ranges dans le dictionnaire texts
    Pour que le texte soit comptabiliser il doit être sur le format suivant :
    
    clé=text

    On peut y mettre des variable tel que %name% qui affiche le nom du joueur
    '''
    global texts
    for f_name in os.listdir(os.getcwd()+"/texts/"):
        with open(os.path.join(os.getcwd()+"/texts/", f_name), 'r', encoding='utf-8') as f:
            for l in f.readlines():
                if(l != None and l != "" and "=" in l):
                    texts[l.split("=")[0]] = l.split("=")[1].replace(r'\n', '\n')
            f.close()

def getTexts():
    '''
    Donne accées au dictionnaire
    '''
    global texts
    return texts

def getText(key : str):
    '''
    Permet d'avoir le contenu d'une clé de mon dictionnaire texts et applique les variables
    '''
    global texts
    return texts[key].replace("%name%", Player.getName()).replace("%hp%", str(Player.getHealth())).replace("%%classe%", Player.getClasse()["name"]).replace("%%exp%", str(Player.getExp())).replace("%%level%", str(Player.getLevel()))