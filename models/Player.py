health = 10
strength = 1
inventory = []
weapon = {}
armor = {}
classe = {}
name = ""
exp = 0

def getHealth():
    '''
    Get la vie du Joueur
    '''
    global health
    return health

def getStrength():
    '''
    Get la force du Joueur
    '''
    global strength
    return strength

def getInventory():
    '''
    Get l'inventaire du Joueur
    '''
    global inventory
    return inventory

def getWeapon():
    '''
    Get l'arme du Joueur
    '''
    global weapon
    return weapon

def getArmor():
    '''
    Get l'armure du Joueur
    '''
    global armor
    return armor

def getClasse():
    '''
    Get la classe du Joueur
    '''
    global classe
    return classe

def getName():
    '''
    Get le nom du Joueur
    '''
    global name
    return name

def getExp():
    '''
    Get le exp du Joueur
    '''
    global exp
    return exp

def setName(na):
    '''
    Set le nom du joueur
    '''
    global name
    name = na

def addInventory(item):
    '''
    Ajouter un item dans l'inventaire
    '''
    global inventory
    inventory.append(item)

def setWeapon(item):
    '''
    Set l'arme du joueur
    '''
    global weapon
    weapon = item

def setNewClasse(name):
    '''
    Set la nouvelle classe du joueur
    '''
    global classe
    classe = {
        "name" : name,
        "exp" : 0
    }

def getLevel():
    '''
    Donne le niveau du joueur
    '''
    global exp
    level = 0
    while(exp > 0):
        exp = exp - (10 * level)
        level = level + 1
    return level