import os
import i18n.Texts as txt
from time import sleep

def launch():
    '''
    Lance le module après le combat avec Gazo
    '''
    os.system("clear")
    print(txt.getText("aftgaz_dialo1"))
    sleep(1)
    print(txt.getText("aftgaz_dialo2"))
    sleep(1)
    print(txt.getText("aftgaz_dialo3"))
    sleep(1) 
    print(txt.getText("aftgaz_dialo4"))
    sleep(1)
    print(txt.getText("aftgaz_dialo5"))
    sleep(1)
    input("Appuyez sur entrée pour continuer...")