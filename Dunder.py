class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def __len__(self):
        return 44


action_figure = Toy('Red', 22)

print(len(action_figure))
print(len('action_figure'))
