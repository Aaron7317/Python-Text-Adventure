class Room:

    #connections is a list of tuples where the first element is room and second element is a direction
    def __init__(self, connections):
        self._connections = connections

    def add_connections(self, new_connections):
        for i in new_connections:
            self._connections.append(i)

    def get_relative_room(self, direction):
        for i in self._connections:
            if direction in i:
                return i[0]

    def room_ability(self):
        print("The room is empty")

    def room_exit(self):
        pass

class Shrine(Room):

    def __init__(self, connections):
        super().__init__(connections)

    def room_ability(self, player):
        player.heal()


