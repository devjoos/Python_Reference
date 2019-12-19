class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        self.name = name
        self.power = power

    def attack(self):
