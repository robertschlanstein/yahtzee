import random

class Dice_cup:
    def __init__(self, num_of_dice = 5):
        self.num_of_dice = num_of_dice
        self.roll = []
        self.keep = []

    def roll_dice(self):
    #make self.roll a new list of rolled dice containing self.keep
        self.roll.clear()
        for d in self.keep:
            self.roll.append(d)
        while len(self.roll) < self.num_of_dice:
            self.roll.append(random.randint(1, 6))

    def keep_dice(self, keep_input):
    #create a list of dice from last roll to keep for next roll
        self.keep.clear()
        for d in self.roll:
            if d in keep_input:
                self.keep.append(d)
                keep_input.remove(d)

class Score_card:
    def __init__(self, num_of_games = 6):
        self.num_of_games = num_of_games
        self.current_game_num = 0
        self.match_scores = []  #list of lists per game containing
                                #the individual scores per turn
        for i in range(num_of_games):   #initialize all score fields
            self.match_scores.append([])
            for j in range(13):
                self.match_scores[i].append(0)
        self.match_sums = [{} for i in range(num_of_games)] #list of dicts per game
                                                            #containing score sums,
                                                            #totals, and the bonus
        self.match_total = 0

    def add_score(self, comb_num, score, game_num):
    #add score for a single turn to match_scores
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

    #functions for calculating sums, totals, bonus
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

    def print_score_card(self):
        print("Upper Section\t", end='')
        for i in range(self.num_of_games):
            print("    #{}".format(i + 1), end='\t')
        print()
        print("1. Aces\t\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[0]), end='\t')
        print()
        print("2. Twos\t\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[1]), end='\t')
        print()
        print("3. Threes\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[2]), end='\t')
        print()
        print("4. Fours\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[3]), end='\t')
        print()
        print("5. Fives\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[4]), end='\t')
        print()
        print("6. Sixes\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[5]), end='\t')
        print()
        print("Sum\t\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[5]), end='\t')
        print()
        print("Bonus\t\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[5]), end='\t')
        print()
        print("Upper\t\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[5]), end='\t')
        print()
        print()
        print("Lower Section")
        print("7. 3 of a Kind\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[0]), end='\t')
        print()
        print("8. 4 of a Kind\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[0]), end='\t')
        print()
        print("9. Full House\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[0]), end='\t')
        print()
        print("10. Sm. Straight", end='')
        for game in self.match_scores:
            print("    {}".format(game[0]), end='\t')
        print()
        print("11. Lg. Straight", end='')
        for game in self.match_scores:
            print("    {}".format(game[0]), end='\t')
        print()
        print("12. Yahtzee\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[0]), end='\t')
        print()
        print("13. Chance\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[0]), end='\t')
        print()
        print("Lower\t\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[5]), end='\t')
        print()
        print("Upper\t\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[5]), end='\t')
        print()
        print("Total\t\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[5]), end='\t')
        print()

def print_game_num(current, total):
    print("GAME {} of {}".format(current, total))

def print_turn_num(current, total):
    print("TURN {} of {}".format(current, total))

def print_roll_num(current, total):
    print("ROLL {} of {}".format(current, total))
