class Dice_cup:
    def __init__(self):
        self.roll = [3, 3, 3, 1, 5]
        self.keep = []

    def roll_dice(self, num):
        self.roll[1] = 1

    def keep_dice(self, keep_input):
        for d in self.roll:
            if d in keep_input:
                self.keep.append(d)
                keep_input.remove(d)

dc = Dice_cup()
dc.keep_dice([3, 3])
print(dc.keep)
