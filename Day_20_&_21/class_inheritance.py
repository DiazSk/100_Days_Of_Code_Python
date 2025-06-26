class Animal:
    def __init__(self):
        # self.num_eyes = 2
        self.swim = "cannot swim"

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.swim = "can swim"

    

nemo = Fish()
print(nemo.swim)

