class User():
    def sign_in(self):
        print('you are signed in')

    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power):
        self._name = name
        self._power = power

    def attack(self):
        print(
            f'I am the all mighty {self._name} and I attacked you with a power of {self._power}')


class Archer(User):
    def __init__(self, name, arrows):
        self._name = name
        self._arrows = arrows

    def attack(self):
        User.attack(self)  # still dont know why we would do this
        print(
            f'They call me {self._name}, my arrow struck you. My arrow count is now: {self._arrows}')

    def run(self):
        print('run really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, _name, power, arrows):
        Archer.attack(self)


hb1 = HybridBorg('Jerry', 132, 99)
print(hb1._arrows)


# wizard1 = Wizard('Merlin', 50)
# archer1 = Archer('Robin', 30)


# def player_attack(char):  # polymorphism
#     char.attack()


# # player_attack(wizard1)
# # player_attack(archer1)

# for char in [wizard1, archer1]:
#     char.attack()
