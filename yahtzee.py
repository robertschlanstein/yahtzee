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
        self.current_game_num = 0
        self.match_scores = []
        for i in range(num_of_games):
            self.match_scores.append([])
            for j in range(13):
                self.match_scores[i].append(0)
        self.match_sums = [{} for i in range(num_of_games)]
        self.match_total = 0

    def add_score(self, comb_num, score, game_num):
        if comb_num < 1 or comb_num > 13:
            print("Invalid combination number...")
            return
        if score < 0 or score > 50:
            print("Impossible score...")
            return
        if self.match_scores[game_num][comb_num - 1] != 0:
            print("Combination already filled in...")
            return
        self.match_scores[game_num][comb_num - 1] = score

    def calc_upper_sum(self, game_num):
        game_sums = self.match_sums[game_num]
        upper_section = self.match_scores[game_num][0:6]
        game_sums["upper_sum"] = sum(upper_section)

    def calc_upper_bonus(self, game_num):
        game_sums = self.match_sums[game_num]
        if game_sums.get("upper_sum", 0) >= 63:
            game_sums["upper_bonus"] = 35
        else:
            game_sums["upper_bonus"] = 0

    def calc_upper_total(self, game_num):
        game_sums = self.match_sums[game_num]
        game_sums["upper_total"] = game_sums["upper_sum"] + game_sums["upper_bonus"]

    def calc_lower_sum(self, game_num):
        game_sums = self.match_sums[game_num]
        lower_section = self.match_scores[game_num][6:13]
        game_sums["lower_sum"] = sum(lower_section)

    def calc_game_total(self, game_num):
        game_sums = self.match_sums[game_num]
        game_sums["game_total"] = game_sums["upper_total"] + game_sums["lower_sum"]
