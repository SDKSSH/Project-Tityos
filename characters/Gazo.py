from random import randint
from i18n.Texts import getText


damage = 1
attacks = ["gazo_at1", "gazo_at2", "gazo_at3", "gazo_at4"]
health = 4

def attack():
    '''
    Gazo attaque mdr
    '''
    if(randint(0,100) >= 90):
        print(getText("attack_tmp") % ("Gazo", getText("gazo_at4"), 667))
        #Win
    else:
        print(getText("attack_tmp") % ("Gazo", getText(attacks[randint(0, 3)]), damage))
