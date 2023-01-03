from time import sleep
import models.Player as Player
from i18n.Texts import getText
import os as os
import modules.ClassChooseModule as clmodule
from pick import pick
import characters.Gazo as Gazo
def launch():
    os.system("clear")
    name = input("Quel est ton nom jeune homme ? ")
    Player.setName(name)
    sleep(0.2)
    print(getText("intro_1"))
    sleep(1.5)
    print(getText("intro_2"))
    sleep(1.5)
    print(getText("intro_3"))
    sleep(1.5)
    print(getText("intro_4"))
    sleep(1.5)
    print(getText("intro_5"))
    sleep(1.5)
    print(getText("intro_6"))
    sleep(1.5)
    print(getText("dg_1"))
    sleep(1.5)
    print(getText("dg_2"))
    sleep(1.5)
    print(getText("dg_3"))
    sleep(1.5)
    input("Appuye sur entrer pour continuer")
    selected = pick([getText("choix_1_o1"), getText("choix_1_o2"), getText("choix_1_o3")], getText("choix_1_n"), indicator="=>")
    clmodule.launch(selected[0][1])
