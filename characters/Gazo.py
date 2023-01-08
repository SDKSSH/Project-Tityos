from random import randint
from i18n.Texts import getText
import models.Player as Player
import combat.Combat as combat

damage = 1
attacks = ["gazo_at1", "gazo_at2", "gazo_at3"]
health = 4
inFight = False

def attack():
    '''
    Gazo attaque
    '''
    if(randint(0,100) >= 90):
        print(getText("attack_tmp") % ("Gazo", getText("gazo_at4"), 667))
        Player.health = 0
    else:
        print(getText("attack_tmp") % ("Gazo", getText(attacks[randint(0, 2)]), damage))
        Player.health = Player.health-damage

def startFight(cb):
    '''
    Lance le combat avec gazo
    '''
    global attack
    combat.startCombat({
        "name" : "Gaz'eau fin gazo jsp",
        "health" : 3,
        "attack" : attack
    }, cb)