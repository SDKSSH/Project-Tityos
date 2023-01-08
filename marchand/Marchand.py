import os
from time import sleep
from pick import pick
import easteregg.doigdrip as doigdrip
import models.Player as Player
import items.Items as Items
def spawnMarchand():
    '''
    Fait apparaître le marchand qui est doigby
    '''
    os.system("clear")
    doigdrip.AfficherDoigby()
    sleep(0.5)
    print("\nDoigby souhaite vous vendre des objets !")
    sleep(2)
    opt = []
    if(Player.getClasse()["name"] == "Guerrier"):
        opt = [4,5,7]
    elif(Player.getClasse()["name"] == "Mage"):
        opt = [3,6,8]
    elif(Player.getClasse()["name"] == "Archer"):
        opt = [9,10, 11]
    options, selected = pick([Items.getItemByID(x) for x in opt], "Que voulez-vous acheter ?", indicator="=>")
    