class Dice_cup:
    def __init__(self, num_of_dice = 5):
        self.num_of_dice = num_of_dice
        self.roll = []
        self.keep = []

    def roll_dice(self, num):
        self.roll[1] = 1

    def keep_dice(self, keep_input):
        for d in self.roll:
            if d in keep_input:
                self.keep.append(d)
                keep_input.remove(d)
