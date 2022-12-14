import models.Player as Player
from i18n.Texts import getText
import os
import items.Items as Items
from time import sleep

def launch(cl):
    '''
    Appelle le module pour le choix de classe
    '''
    os.system("clear")
    sleep(0.8)
    if(cl == 0):
        print(getText("mage_ch"))
        Player.setWeapon(Items.sceptre_defaillant)
        Player.setNewClasse("Mage")
    if(cl == 1):
        print(getText("guerrier_ch"))
        Player.setWeapon(Items.epee_briser)
        Player.setNewClasse("Guerrier")
    if(cl == 2):
        print(getText("archer_ch"))
        Player.setWeapon(Items.lance_pierre)
        Player.setNewClasse("Archer")
