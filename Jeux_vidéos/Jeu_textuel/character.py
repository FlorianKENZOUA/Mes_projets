'''
Ce module permet de définir la classe Character
'''
import random

class Character:
    '''
    La classe Character permet de définir des PNJ dans le jeu qui sont
    représentés par un nom, une description, la pièce dans laquelle ils se trouvent
    et des répliques pour le dialogue.

    Attributes:
        name (str): le nom du PNJ
        description (str): la description du PNJ
        current_room (Room) : la pièce dans laquelle le PNJ se trouve
        msgs (List) : liste des répliques que le PNJ peut dire

    Methods:
        __init__(self, name,description,current_room, msgs) : The constructor.
        __str__(self) : The string representation of the PNJ.
    '''
    def __init__(self,name,description,current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs

    def __str__(self):
        return str((str(self.name) +" : " + str(self.description)))

    def move(self):
        '''
        Permet aux PNJ de se déplacer de pièce en pièce

        Aucun attribut

        Retourne True (Bool)
        '''
        move = random.choice([True, False])

        if not move:
            return False

        rooms = self.current_room.exits.values()

        if not rooms:
            return False

        new_room = random.choice(rooms)
        self.current_room = new_room
        return True

    def get_msg(self, character_name):
        '''
        Permet d'avoir un msg du PNJ

        Attribut : 
            - character_name (str)
        
            Retourne None (Bool)
        '''
        for character in self.current_room.characters:
            if character.name == character_name:
                msg = character.msgs.pop(0)  
                character.msgs.append(msg)
                return msg
        print(f" '{character_name}' introuvable.")
        return None