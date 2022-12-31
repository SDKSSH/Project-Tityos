from random import randint
from i18n.Texts import getText
from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC,SND_ALIAS
import models.Player as Player
import os


damage = 1
attacks = ["gazo_at1", "gazo_at2", "gazo_at3", "gazo_at4"]
health = 4
inFight = False

def playGazoTheme():
    PlaySound(os.getcwd().replace("//", "/")+'/sounds/gazo/gazoTheme.wav', SND_LOOP|SND_ASYNC|SND_FILENAME)

def stopGazoTheme():
    PlaySound(None, SND_FILENAME)

def attack() -> bool:
    '''
    Gazo attaque
    Il retourne a la fin si le fight continue ou est perdu
    '''
    if(randint(0,100) >= 90):
        print(getText("attack_tmp") % ("Gazo", getText("gazo_at4"), 667))
        stopGazoTheme()
        return False
    else:
        print(getText("attack_tmp") % ("Gazo", getText(attacks[randint(0, 3)]), damage))
        Player.health = Player.health-damage
        if Player.health <= 0:
            return False
        else:
            return True