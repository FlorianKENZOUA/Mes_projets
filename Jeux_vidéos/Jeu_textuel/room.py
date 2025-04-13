# Define the Room class.
'''
Ce module permet de définir la classe Room
'''

class Room:
    """
    Cette classe représente les différentes salles accessibles. Une salle est définie 
    par son nom "name" et sa description "description"
    
    Attributs:
        name (str) : Le nom de la salle
        description (str) : la description de ce que contient la salle
        direction (str) : Correspond à une direction à suivre ( NORD, SUD, EST, OUEST)
    
    Méthodes:
        __init__(self,name,description) : Le constructeur
        get_exit(self,direction) : Donne la sortie qu'on obtient pour une direction 
        donnée ( si la sortie existe )
        get_exit_string(self) : Donnes les différentes sorties possibles pour la salle 
        dans laquelle on se trouve
        get_long_description(self) : Donne la description de la salle ainsi que les 
        différentes sorties possibles
    
    Examples:

    >>> room = Room("nom de la salle", "description de la salle" )
    >>> room.name
    "nom de la salle"
    >>> room.description
    "description de la salle"
    """
    # Define the constructor.
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = set()
        self.characters = set()

    def __str__(self):
        return f"{self.name}"
    # Define the get_exit method.
    def get_exit(self, direction):
        '''
        Permet d'avoir les directions disponibles

        Aucun argument

        Retourne None (Bool)
        '''
        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None

    # Return a string describing the room's exits.
    def get_exit_string(self):
        '''
        Permet d'avoir les directions disponibles en str

        Aucun argument

        Retourne exit_string (str)
        '''
        exit_string = "Sorties: "
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        '''
        Permet d'avoir une description de la pièce

        Aucun argument

        Retourne la description de la pièce dans le terminal
        '''
        return f"\n{self.description}\n\n{self.get_exit_string()}\n"

    def get_inventory(self):
        '''
        Permet d'avoir l'inventaire de la pièce

        Aucun argument

        Retourne string
        '''
        if self.inventory == set():
            print("Il n'y a rien ici !")
        else:
            print("La pièce contient :")
            for i in self.inventory:
                print("-\t" + str(i))
    

    def get_character(self):
        '''
        Permet d'avoir l'inventaire de la pièce

        Aucun argument

        Retourne string
        '''
        if self.characters == set():
            print("Il n'y a personne ici !")
        else:
            print("La pièce contient :")
            for i in self.characters:
                print("-\t" + str(i))

