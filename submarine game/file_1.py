import random
from enum import Enum


class Utility:
    def __init__(self):
        self.ship_prefix = ['Undefeated', 'Silent', 'Brave', 'Steel', 'Nimble', 'Mighty', 'Shadow', 'Swift']
        self.ship_name = ['Seahawk', 'Stingray', 'Leviathan', 'Barracuda', 'Kraken', 'Neptune', 'Thunder', 'Tempest']
        self.room_names = ["torpedo room", "sonar room", "engine room", "navigation room", "Supplies room", "captain room"]

    def generate_submarine_name(self):
        """ Generates a two part name for the player's submarine. """
        prefix = random.choice(self.ship_prefix)
        name = random.choice(self.ship_name)
        return f"{prefix} {name}"


class Menus:
    def __init__(self):
        self.starting_options = ["What would you like to do next?:", "(1) Set Sail",
                                 "(2) Check the ship's stores", "(3) Visit your cabin."]

    def display_starting_menu(self):
        """ Presents the player their options at the beginning of the game. """
        for text in self.starting_options:
            print(text)
        choice = input("What is your decision Captain?: ")
        match choice:
            case "1":  # set sail
                pass
            case "2":  # check ship stores
                pass
            case "3":  # visit cabin
                pass
            case _:
                print("That option is not available Captain.")


class Player(Utility):
    def __init__(self):
        Utility.__init__(self)
        self.name = input("What is your name Captain?:")
        self.ship_name = self.generate_submarine_name()
        print(f"Welcome aboard the {self.ship_name} Captain{self.name}!")


class RoomState(Enum):
    """ Class that contains the different states that any room on the submarine can be in. """
    NORMAL = "normal"
    LIGHTLY_DAMAGED = "lightly damaged"
    DAMAGED = "damaged"
    HEAVILY_DAMAGED = "heavily damaged"
    FLOODED = "flooded"


class Room:
    def __init__(self, name, state=RoomState.NORMAL):
        """ Base Class for all rooms on the submarine. """
        self.name = name
        self.state = state

    def set_state(self, new_state):
        self.state = new_state

    def get_state(self):
        return self.state.value
    

class SubmarineMovementState:
    DIVING = False
    RISING = False
    MOVING_FORWARD = False
    MOVING_BACKWARD = False
    STATIONARY = False


class Submarine(Player, Utility):
    def __init__(self, state=SubmarineMovementState.STATIONARY):
        Player.__init__(self)
        Utility.__init__(self)
        self.rooms = self.create_new_submarine()
        self.move_state = state
        self.depth = 0        # MIGHT MAKE THIS AND SELF.VELOCITY INTO A TUPLE OR ENUM
        self.velocity = 0

    def set_movement_state(self, new_move_state):
        """ Sets the current movement state of the submarine. """
        self.move_state = new_move_state

    def create_new_submarine(self) -> dict:
        """ Creates all the rooms needed for a new submarine. """
        rooms = {}  # Empty dictionary to store the sub's rooms
        key = 1  # Counter for generating unique keys for each new room created
        for name in self.room_names:
            new_room = Room(name)
            rooms[key] = new_room
            key += 1
        return rooms
