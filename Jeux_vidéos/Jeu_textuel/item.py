'''
Ce module permet de définir la classe Item
'''

class Item:
    '''
    Cette classe permet de représenter un objet définit par un nom, une desciption
    et un poids.

    Attributs :
    name : str 
    description : str 
    weight : float 

    Méthodes :
    __init__(self, name: str, description: str, weight: float) 
    __str__(self) -> str 
    '''
    def __init__(self,name,description,weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        return str((str(self.name) +" : " + str(self.description) +
                    " ( " + str(self.weight) + "kg )"))
