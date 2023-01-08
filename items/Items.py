from typing import Optional


epee_briser = {
    "id" : 0,
    "name" : "Épée Briser",
    "damage" : 1,
    "sell" : 0
}
sceptre_defaillant = {
    "id" : 1,
    "name" : "Sceptre Défaillant",
    "damage" : 1,
    "sell" : 0
}
lance_pierre = {
    "id" : 2,
    "name" : "Lance Pierre En Bois De Sapin",
    "damage" : 1,
    "sell" : 0
}

sceptre_brillant = {
    "id" : 3,
    "name" : "Sceptre Brillant",
    "damage" : 2,
    "sell" : 0
}

epee_en_bois = {
    "id" : 4,
    "name" : "Épée En Bois",
    "damage" : 2,
    "sell" : 0
}

epee_en_metal = {
    "id" : 5,
    "name" : "Épée En Métal",
    "damage" : 4,
    "sell" : 0
}

sceptre_metalique = {
    "id" : 6,
    "name" : "Sceptre Métallique",
    "damage" : 5,
    "sell" : 0
}

epee_lunatique = {
    "id" : 7,
    "name" : "Épée Lunatique",
    "damage" : 8,
    "sell" : 0
}

sceptre_de_lumiere = {
    "id" : 8,
    "name" : "Sceptre De Lumière",
    "damage" : 10,
    "sell" : 0
}

arc_neuf = {
    "id" : 9,
    "name" : "Arc Neuf",
    "damage" : 2,
    "sell" : 0
}

arc_en_bois = {
    "id" : 10,
    "name" : "Arc En Bois",
    "damage" : 4,
    "sell" : 0
}

arc_sacre = {
    "id" : 11,
    "name" : "Arc Sacré",
    "damage" : 10,
    "sell" : 0
}

def getItemByID(id : int) -> Optional[dict]:
    '''
    Get an item by its ID
    >>> getItemByID(1)
    {'id': 0, 'name': 'Épée Briser', 'damage': 1, 'sell': 0}
    '''
    f_dict = {k:v for k,v in globals().items() if isinstance(v, dict) and "id" in v and "damage" in v and v["id"] == id}
    l = list(f_dict.values())
    if(len(l) == 0):
        return None
    else:
        return l[0]