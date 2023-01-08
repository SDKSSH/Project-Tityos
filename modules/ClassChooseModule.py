import models.Player as Player
from i18n.Texts import getText
import os
import items.Items as Items
import modules.AfterGazoCombatModule as agcm
from time import sleep
import characters.Gazo as Gazo

def launch(cl):
    global lol
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
    sleep(1)
    print(getText('act_1'))    
    sleep(1)
    print(getText('dg_4'))
    sleep(1)
    print(getText('dg_5'))
    sleep(1)
    print(getText('dg_6'))
    sleep(1)
    print(getText('dg_7'))
    sleep(1)
    print(getText('dg_8'))
    sleep(1)
    print(getText('dg_9'))
    sleep(1)
    print(getText('dg_10'))
    sleep(1)
    print(getText('dg_11'))
    sleep(1)
    print(getText('dg_12'))
    sleep(1)
    print(getText('dg_13'))
    input("Appuye sur Entrer pour commencer le combat")
    Gazo.startFight(agcm.launch)
