class Tamagotchi:
    def __init__(self, name, birthday):
        self.name = name
        self.hunger = 100
        self.energy = 100
        self.birthday = birthday
        self.age = 0
        self.cash = 20
        self.happiness = 0
        self.loan = 0
        self.exercise = 0
        self.drunk = 0
        self.dead = False
        self.warning = False
        self.asleep = False
        self.buy = False

        self.hunger_state = True
        self.energy_state = False
        self.popup_state = False
        


    def update(self):
        self._energy(-1)
        self._hunger(-3)


    def _hunger(self, change = -3):
        #hunger logic
        self.hunger += change
        if self.hunger > 100:
            self.hunger = 100
        if self.hunger <= 0:
            self.gameover()

    
    def _eat(self):
        self._hunger(40)


    def _energy(self, change = -1):
        if self.energy > 0 and self.energy <= 100:
            self.energy += change
        elif self.energy > 100:
            self.energy = 100
        else:
            print('Sleeping')
            self._sleep()


    def _sleep(self):
        self.energy = 100
        self.asleep = True

    def gameover(self):
        self.dead = True
        print('Game over')

