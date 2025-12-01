class Dice_cup:
    def __init__(self):
        self.roll = [0, 0, 0, 0, 0]
        self.keep = []

    def roll_dice(self, num):
        self.roll[1] = 1

    def keep_dice(self, keep_list):
        self.keep = sorted(keep_list[:len(self.roll)])

dc = Dice_cup()
dc.keep_dice([])
print(dc.keep)
