from time import sleep
import models.Player as Player
from pick import pick
import easteregg.doigdrip as doigdrip

def startCombat(rival, callback):
    '''
    Lance un combat contre un rival
    '''
    defense = False
    print("Le combat commence !!!!")
    sleep(1)
    round = 1
    end = False
    while(end == False):
        if(round%2 == 1):
            options, selected = pick(['Attaquer', 'Défendre', "Doigdrip l'ennemie"], "Vous attaquez "+rival["name"]+" ! Il lui reste "+str(rival["health"])+" HP !\nStats:\nHP: %s | Epée: %s" % (Player.getHealth(), Player.getWeapon()["name"]), indicator="=> ")
            if selected == 0:
                rival["health"] = rival["health"]-Player.getStrength()
                print("Tu as attaquer %s, il lui reste %s HP" % (rival["name"], rival["health"]))
                if(rival["health"] <= 0):
                    end = True
            if selected == 1:
                defense = True
                print("Tu te défend face à %s !" % (rival["name"]))
            if selected == 2:
                doigdrip.AfficherDoigby()
                print("Get doigdriped ahahahaha !")
                Player.health = Player.health-1
                if(Player.health <= 0):
                    end = True
        else:
            print("Au tour de %s d'attaquer !" % (rival["name"]))
            sleep(0.5)
            if(defense == True):
                print("%s a mis en place sa défense donc il prend 0 dégat !" % (Player.getName()))
                defense = False
            else:
                rival["attack"]()
                if(Player.getHealth() <= 0):
                    end = True
            sleep(1.667)
        round = round+1
    if(Player.health > 0):
        Player.exp = Player.exp+rival["exp"]
        print("Tu as gagné ce combat ! Tu remporte %s exp" % (rival["exp"]))
        sleep(1.5)
        callback()
    else:
        print("GAME OVER !!!")
        exit()