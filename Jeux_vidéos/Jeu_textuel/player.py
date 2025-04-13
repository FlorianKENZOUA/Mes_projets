# Define the Player class.
'''
Ce module permet de définir la classe Player
'''
class Player():
    """
    Cette classe représente un joueur. Un joueur est composé d'un nom et une direction.

    Attributs :
        name (str): Le nom du playeur.
        direction (str): La direction à suivre.
        history (list) : liste des salles visitées

    Méthodes :
        __init__(self, name) : Le constructeur.
        move(self, direction) : Définir la méthode de déplacement.

    Exemples :

    >>> player = Player("Arthur" , "N",["Village"])
    >>> player.name
    'Arthur'
    >>> player.direction
    'N'
    >>> player.direction
    ["Village"]
    """

    # Define the constructor.
    history = []
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.inventory = {}
        self.max_weight = 25


    def get_history(self,history):
        '''
        Permet d'avoir l'historique de visite'

        Arguments :
            - history (List) : liste des lieux visités

        Retourne rien
        '''
        print("\n Vous avez déja visité les pièces suivantes:")
        for i in history:
            print("-\t" + str(i) )


    # Define the move method.
    def move(self, direction):
        '''
        Permet de se déplacer 

        Arguments :
            - direction (str) : direction cardinale utilisée par le joueur

        Retourne True ou False (Bool)
        '''
        # Get the next room from the exits dictionary of the current room.
        if direction in self.current_room.exits:
            next_room= self.current_room.exits[direction]

            if next_room is None:
                print("\nCette direction n'existe pas\n")
                return False
            else:
                self.history.append(self.current_room)
                self.current_room = next_room
                print(f"{self.current_room.name}")
        else:
            print(f"La commande de direction '{direction}' n'est pas valide !")
            return False

        print(self.current_room.get_long_description())
        self.get_history(self.history)
        return True

    def get_inventory(self):
        '''
        Permet d'avoir le contenu de son inventaire

        Aucun argument

        Retourne rien
        '''
        if self.inventory =={}:
            return print("Votre inventaire est vide !")
        else:
            print("\n Votre inventaire contient :")
            for i in self.inventory.keys():
                print("-\t" + str(i) )
