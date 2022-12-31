from random import randint
from i18n.Texts import getText
import multiprocessing
from playsound import playsound
import models.Player as Player


damage = 1
attacks = ["gazo_at1", "gazo_at2", "gazo_at3", "gazo_at4"]
health = 4
inFight = False
sound_thread = None

def playGazoTheme():
    global sound_thread
    sound_thread = multiprocessing.Process(target=playsound, args=("sounds/gazo/gazoTheme.mp3",))
    sound_thread.start()
    
def stopGazoTheme():
    global sound_thread
    sound_thread.close()
    sound_thread = None

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