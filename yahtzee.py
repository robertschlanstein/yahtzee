import random

class Dice_cup:
    def __init__(self, num_of_dice = 5):
        self.num_of_dice = num_of_dice
        self.roll = []
        self.keep = []

    def roll_dice(self):
        self.roll.clear()
        print(self.roll)
        for d in self.keep:
            self.roll.append(d)
        print(self.roll)
        while len(self.roll) < self.num_of_dice:
            self.roll.append(random.randint(1, 6))
        print(self.roll)

    def keep_dice(self, keep_input):
        for d in self.roll:
            if d in keep_input:
                self.keep.append(d)
                keep_input.remove(d)

dc = Dice_cup()
dc.roll_dice()
