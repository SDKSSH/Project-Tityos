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