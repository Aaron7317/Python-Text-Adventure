class Character:

    def __init__(self, level, starting_money):
        self._money = starting_money
        self._max_health = level * 4
        self._health = level * 4
        self._level = level
        self._exp = 0;

    def calculate_damage(self):
        pass

    def heal(self, amount=None):
        if amount is not None:
            self._health += amount
        if self._health > self._max_health or amount is None:
            self._health = self._max_health
        
    def get_damage(self):
        return self._level + 1


class Enemy(Character):

    def __init__(self, level, starting_money=5):
        super().__init__(level)

            
class Player(Character):
    
    def __init__(self, level, starting_money=10):
        super().__init__(level)

    def get_damage(self, item_damage):
        return self._level + item_damage


    