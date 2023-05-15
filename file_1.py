class Room:
    def __init__(self, name, key, status=None):
        self.name = name
        self.status = status
        self.key = key
        self.is_flooded = False
        self.is_damaged = False
        self.is_intact = False

    def set_state(self, state: int):
        """ Sets the current state of the room."""
        if state is 1 or 0:
            self.is_intact = True
        if state is 2:
            self.is_damaged = True
        if state is 3:
            self.is_flooded = True


class Torpedo:
    def __init__(self, name, best_ship):
        self.name = name
        self.best_ship = best_ship
        pass



class TorpedoTube:
    def __init__(self, name, is_loaded):
        self.is_loaded = is_loaded
        self.name = name

        pass


class TorpedoRoom:
    def __init__(self, num_of_tubes):
        self.tubes = self.create_torp_tubes(num_of_tubes)


    def create_torp_tubes(self, num):
        tubes = dict()
        for i in range(num)


class ControlRoom:
    pass


class SonarRoom:
    pass


class EngineRoom:
    pass


class FoodStores:
    pass


class CaptainQuarters:
    pass
