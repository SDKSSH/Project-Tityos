import i18n.Texts as txt
import easteregg.doigdrip as doigdrip

def launch():
    '''
    Permet de load tous les textes son etc...
    '''
    txt.loadTexts()
    doigdrip.lireFichier()
