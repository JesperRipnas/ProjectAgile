class Tamagotchi:
    def __init__(self, name, birthday):
        self.name = name
        self.hunger = 100
        self.energy = 100
        self.birthday = birthday
    
    def update(self):
        self._energy()
        self._hunger()


    def _hunger(self, change = -3):
        #hunger logic
        self.hunger += change
        if self.hunger > 100:
            self.hunger = 100
        if self.hunger <= 0:
            self. hunger = 0
            #dying die()?
        print(self.hunger)
    

    def _eat(self):
        self._hunger(40)


    def _energy(self):
        1 + 1
        #energy logic

