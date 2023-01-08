import os
from time import sleep
from pick import pick
import easteregg.doigdrip as doigdrip
import models.Player as Player
import items.Items as Items
def spawnMarchand(cb):
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
    it = Items.getItemByName(options)
    sendPick(opt, cb)

def sendPick(opt, cb):
    '''
    Envoie un pick avec les options
    '''
    optt = [Items.getItemByID(x) for x in opt]
    optt.append("Quitter")
    options, selected = pick(optt, "Que voulez-vous acheter ?", indicator="=>")
    if(options == "Quitter"):
        cb()
    else:
        it = Items.getItemByName(options)
        if(Player.getMoney() >= it["price"]):
            Player.removeCoin(it["price"])
            Player.setWeapon(it)
            print("Vous avez acheté %s" % (it["name"]))
            sleep(1)
        else:
            print("Vous n'avez pas assez d'argent !")
            sleep(1)
            sendPick(opt)