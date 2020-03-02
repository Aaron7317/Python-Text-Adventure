import sys

def singleton(myClass):
	instances = {}
	def getInstance(*args, **kwargs):
		if myClass not in instances:
			instances[myClass] = myClass(*args, **kwargs)
		return instances[myClass]
	return getInstance


@singleton
class Game:
    
    _game_states = ["intro", "standard_turn", "combat_turn"]

    def __init__(self, initial_game_state):
        self._game_state = initial_game_state

    def set_game_state(self, new_state):
        if new_state.lower() in _game_states:
            self._game_state = new_state

    def execute_game_state(self):
        try:
            self._game_states[self._game_state]()
        except NameError:
            print("Error! Current game state does not exist!")
            sys.exit()

    def intro(self):
        pass

    def normal_turn(self):
        pass

    def combat_turn(self):
        pass 