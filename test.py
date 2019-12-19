class PlayerCharacter():
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def _speak(self):
        print(F'hello my name is {self._name} and I am {self._age} years old')


class TestThis(PlayerCharacter):
    pass


player1 = PlayerCharacter("jimmy", 32)
test1 = TestThis("dik", 33)
print(test1._name)

player1._speak()
