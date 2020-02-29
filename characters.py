class Character:

    def __init__(self, max_health, level):
        self._max_health = max_health
        self._health = max_health
        self._level = level
        self._exp = 0;

    def calculate_damage(self):
        pass

    def heal(self, amount=None):
        if amount is None:
            

            
