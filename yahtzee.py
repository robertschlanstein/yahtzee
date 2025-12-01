import random

class Dice_cup:
    def __init__(self, num_of_dice = 5):
        self.num_of_dice = num_of_dice
        self.roll = []
        self.keep = []

    def roll_dice(self):
        self.roll.clear()
        for d in self.keep:
            self.roll.append(d)
        while len(self.roll) < self.num_of_dice:
            self.roll.append(random.randint(1, 6))

    def keep_dice(self, keep_input):
        self.keep.clear()
        for d in self.roll:
            if d in keep_input:
                self.keep.append(d)
                keep_input.remove(d)

class Score_card:
    def __init__(self, num_of_games = 6):
        self.num_of_games = num_of_games
        self.match_scores = []
        self.match_sums = []
        self.match_total = 0

    def new_game(self):
        self.match_scores.append([0 for i in range(13)])

    def add_score(self, comb_num, score):
        if comb_num < 1 or comb_num > 13:
            print("Invalid combination number...")
            return
        if score < 0 or score > 50:
            print("Impossible score...")
            return
        if self.match_scores[-1][comb_num - 1] != 0:
            print("Combination already filled in...")
            return
        self.match_scores[-1][comb_num - 1] = score
        print(self.match_scores)

    def sum_upper_section():
        pass

    def sum_lower_section():
        pass

    def calc_bonus():
        pass

    def sum_total_score():
        pass

sc = Score_card()
