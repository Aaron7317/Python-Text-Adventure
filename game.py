

def singleton(myClass):
	instances = {}
	def getInstance(*args, **kwargs):
		if myClass not in instances:
			instances[myClass] = myClass(*args, **kwargs)
		return instances[myClass]
	return getInstance


@singleton
class Game:
    
    __game_states = ["INTRO", "STANDARDTURN", "COMBATTURN"]

    def __init__(self, initial_game_state):
        self.__game_state = initial_game_state

    def set_game_state(self, new_state):
        if new_state in __game_states:
            self.__game_state = new_state

    def execute_current_state(self):
        pass