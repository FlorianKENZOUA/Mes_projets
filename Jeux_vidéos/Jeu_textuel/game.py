# Description: Game class
'''
Ce module permet de décrire la classe Game
'''
# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character

class Game:
    '''
    La classe Game est organisée de la façon suivante :
    Attributs :
    finished : bool 
    rooms : List[Room] 
    commands : Dict[str, Command] 
    player : Player 
    Méthodes :  
    __init__() 
    setup() 
    play() 
    process_command(command_string : str) -> None 
    print_welcome() 
    '''
    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None

    # Setup the game
    def setup(self):
        '''
        Cette fonction permet d'établir le setup du jeu

        Retourne rien

        aucun argument
        '''
        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)",
                      Actions.go, 1)
        self.commands["go"] = go
        history = Command("history",": historique des lieux visités ",Player.get_history, 0)
        self.commands["history"] = history
        back = Command("back","Permet de retourner à la direction précédente",Actions.back,0)
        self.commands["back"] = back
        look = Command("look","Permet de voir les items aux alentours",Actions.look,0)
        self.commands["look"] =  look
        take = Command("take","Permet de récuperer les objets aux alentours",Actions.take,1)
        self.commands["take"] = take
        check = Command("check", " Permet de voir le contenu de son inventaire",Actions.check,0 )
        self.commands["check"] = check
        drop = Command("drop","Permet de se débarasser d'un item présent dans son inventaire",
                       Actions.drop,1)
        self.commands["drop"] = drop
        talk = Command("talk","Permet de parler avec un PNJ",Actions.talk,1)
        self.commands["talk"] = talk
        unlock = Command("unlock","Permet de dévérouiller un code à 4 chiffres",Actions.unlock,1)
        self.commands["unlock"] = unlock
        # Setup rooms
        Volcan = Room("Volcan", "Vous vous trouvez au sommet du volcan, vous apercevez"
                      +" au loin plusieurs lieux différents. A l'est, vous apercevez une"
                      +" plage qui semble animée. Au sud, vous apercevez un village. Enfin"
                       +" à l'est vous apercevez une immense jungle. Il serait judicieux"
                       +" de quitter le Volcan au plus vite et d'éviter de vous approchez du bord.")
        self.rooms.append(Volcan)

        Chemin = Room("Sentier de terre", "Vous êtes sur un sentier de terre, au sud il vous "
                      +"mène vers un village, à l'ouest vers une plage et à l'est vers une jungle")
        self.rooms.append(Chemin)

        Bord = Room("Bord du volcan", " Vous vous approchez doucement du bord du volcan lorsque"
                    + " vous êtes soudainenement pris de panique après avoir entendu un bruit "
                    +"effrayant, vous glissez et vous tomber dans la lave. Vous êtes mort, il "
                    +"ne fallait décidément pas s'approcher du bord...")
        self.rooms.append(Bord)

        Plage = Room("Plage", " Vous arrivez sur une plage bondée de monde. Vous apercevez un"
                     + " camion de glace, un terrain de volley et un peu plus loin un feu de "
                     +"camps. Vous remarquez aussi que le chemin reliant la Plage au Volcan "
                     +"n'est plus accessible " )
        self.rooms.append(Plage)

        Village = Room("Village", " Vous arrivez dans un village où vous êtes rapidement "
                       +"acceuilli par les habitants qui vous proposent de faire le tour "
                       +"du village. Vous pouvez visiter la mairie ou en "
                       +"cas de faim aller vous restaurer en Kebab du coin" )
        self.rooms.append(Village)

        Jungle = Room("Jungle", " Vous arrivez dans une impressionnante Jungle. Vous apercevez "
                      +"une cabane perchée au loin, une grotte souterraine qui ne demande "
                      +"qu'à être explorée et un impressionant arbre vieux de plus de 100ans")
        self.rooms.append(Jungle)

        Kebab = Room(" Keb à Bord", "Vous arrivez au 'Keb à Bord', un délicieux restaurant "
                     +"mais l'établissement est vide ")
        self.rooms.append(Kebab)

        Mairie = Room(" Mairie du village ", " Vous arrivez dans la Mairie du Village, vous "
                      +"apercevez quelqu'un a l'accueil. Souhaitez-vous aller le voir ?" )
        self.rooms.append(Mairie)

        Ferme = Room(" Ferme du village", " Vous arrivez dans la ferme du village. "
                     +"Il n'y a personne ici ")
        self.rooms.append(Ferme)

        Cabane = Room(" Cabane perchée ", " Vous êtes au pied d'une cabane perchée, "
                      +"souhaitez-vous y monter ? " )
        self.rooms.append(Cabane)

        Grotte = Room("Grotte souterraine", " Vous arrivez devant une grotte souterraine, "
                      +"souhaitez-vous y descendre ? " )
        self.rooms.append(Grotte)

        Arbre = Room(" Arbre de 100 ans " , " Vous arrivez devant l'arbre de 100 ans, vous "
                     +"apercevez quelque chose au pied de l'arbre." )
        self.rooms.append(Arbre)

        Glace = Room("Marchand de glace", " Vous arrivez devant le camion de glace. Vous "
                     +"avez très chaud. Souhaitez-vous vous rafraichir ? ")
        self.rooms.append(Glace)

        Feu = Room("Feu de camps ", " Vous arrivez au niveau d'un feu de camps desert. Vous "
                   +"apercevez quelqu'un. " )
        self.rooms.append(Feu)

        Volley = Room("Terrain de Volley", " Vous arrivez sur un terrain de volley. Il "
                      +"semblerait que le terrain soit vide ")
        self.rooms.append(Volley)

        Interieur = Room("Interieur", " Vous arrivez à l'interieur de la cabane, vous apercevez une boite vérouillé avec un code à 4 chiffre. Vous avez un essaie. Pour tenter de déverouiller la boite utiliser la commande : unlock [CODE]")
        self.rooms.append(Interieur)

        Fgrotte = Room( " Fond de la grotte", " Vous êtes dans le fond de la grotte")
        self.rooms.append(Fgrotte)

        # Create exits for rooms

        Interieur.exits={"D": Cabane, "N" : None, "E" :None, "S" : None, "O" : None,"U": None}

        Volcan.exits = {"D": Chemin, "N" : None, "E" :None, "S" : None, "O" : None,"U": Bord}

        Plage.exits = {"D": None, "N" : Glace, "E" :Chemin, "S" : None, "O" : None,"U": None}

        Feu.exits = {"D":   None, "N" : None, "E" :None, "S" : Glace, "O" : None,"U": None}

        Volley.exits = {"D": None, "N" : None, "E" :Glace, "S" : None, "O" : None,"U": None}

        Glace.exits = {"D": None, "N" : Feu, "E" :None, "S" : Plage, "O" : Volley,"U": None}

        Village.exits = {"D": None, "N" : Chemin, "E" :None, "S" : Kebab, "O" : Mairie,"U": None}

        Mairie.exits = {"D": None, "N" : None, "E" :Village, "S" : Ferme, "O" : None,"U": None}

        Ferme.exits = {"D": None, "N" : Mairie, "E" :Kebab, "S" : None, "O" : None,"U": None}

        Kebab.exits = {"D": None, "N" : Village, "E" :None, "S" : None, "O" : Ferme,"U": None}

        Cabane.exits = {"D": None, "N" : None, "E" :None, "S" : None, "O" : Jungle,"U": Interieur}

        Jungle.exits = {"D": None, "N" : None, "E" :Cabane, "S" : None, "O" : Chemin,"U": None}

        Grotte.exits = {"D": Fgrotte, "N" : Jungle, "E" :None, "S" : None, "O" : None,"U": None}

        Fgrotte.exits = {"D": None, "N" : None, "E" :None, "S" : None, "O" : None,"U": Grotte}

        Chemin.exits = {"D": None, "N" : None, "E" :Jungle, "S" : Village, "O" : Plage,"U": Volcan}

        bague6 = Item("bague","Le chiffre 6 est gravé sur la bague",1)
        bague2= Item("bague","Le chiffre 2 est gravé sur la bague",1)
        bague9 = Item("bague","Le chiffre 9 est gravé sur la bague",1)
        bague5= Item("bague","Le chiffre 5 est gravé sur la bague",1)
        Mairie.inventory.add(bague6)
        Glace.inventory.add(bague2)
        Jungle.inventory.add(bague9)
        Feu.inventory.add(bague5)
        Aventurier = Character("Aventurier","Un aventurier qui semble cherche quelque chose",Volcan,["Salut, tu as trouvé la boite ?","Comment ça tu ne sais pas de quoi je parle ? Tu ne participes pas au jeu de piste ?"," Tu devrais essayer ! Une boite verouillé par un code est caché sur l'ile, trouve la boite et trouve le code et tu auras gagné le jeu de piste !" ])
        Volcan.characters.add(Aventurier)
        Horloger = Character("Horloger","Un drôle d'horloger qui semble garder une bague",Mairie, ["Tu peux prendre ma bague si tu le souhaite, elle porte en gravure le chiffre 6","Il n'y a plus rien à voir ici, pars ! ", " Bon... Puisque tu ne veux pas partir, voici une énigme : Quand sonne midi, le cercle commence ici."])
        Mairie.characters.add(Horloger)
        Voyageur = Character("Voyageur","Un drôle de voyageur qui semble garder une bague",Glace, ["Tu peux prendre ma bague si tu le souhaite, elle porte en gravure le chiffre 2","Il n'y a plus rien à voir ici, pars ! ", " Bon... Puisque tu ne veux pas partir, voici une énigme : Entre le premier et l'avant-dernier, je garde le silence."])
        Glace.characters.add(Voyageur)
        Marchand = Character("Marchand","Un marchand qui semble se promener",Jungle, ["Salut, je suis un riche marchand ! ","QUOI ?! Tu penses que je mens ?! Dans ce cas je vais t'offrir ma bague en guise de preuve ! Elle est gravé avec le numéro 9","Avant que tu partes voici une énigme : Après le silence je fais des vagues"])
        Jungle.characters.add(Marchand)
        Marin = Character("Marin","Un marin qui se repose au coin du feu",Feu,["Salut, j'ai trouvé une bague en mer, je te l'offre. Elle est gravé avec le numéro 5","Dis-moi, tu aimes les énigmes ? En voici une : Quand tout est dit, c'est moi qui clos l'aventure"])
        Feu.characters.add(Marin)

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = Volcan

    # Play the game
    def play(self):
        '''
        Fonction permettant de faire tourner le jeu

        Aucun argument

        Retourne None (Bool)
        '''
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        '''
        Permet de traiter les commandes appelées par le joueur

        Arguments :
            - command_string (str) : commande appelée par le joueur

        Retourne rien
        '''
        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print("")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        '''
        Permet de souhaiter la bienvenue au joueur et de démarrer le jeu

        Aucun argument

        Retourne rien
        '''
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())


def main():
    '''
    Lancement du jeu
    '''
    # Create a game object and play the game
    Game().play()


if __name__ == "__main__":
    main()
